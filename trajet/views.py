from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Trajet
from .forms import RechercheForm, TrajetForm
from client.models import Client
from django.contrib import messages

def recherche(request):
    pointDepart = request.GET.get('pointDepart')
    pointArrivee = request.GET.get('pointArrivee')
    date = request.GET.get('date')
    trajets = Trajet.objects.filter(pointDepart=pointDepart, pointArrivee=pointArrivee, date=date)
    return render(request, 'trajet/recherche.html', {'trajets': trajets})

def reserver(request, trajet_id):
    client_id = request.session.get('client_id')
    if not client_id:
        return redirect('connexion')
    
    client = get_object_or_404(Client, id=client_id)
    if not client.is_active:
        messages.error(request, "Votre compte est suspendu. Vous ne pouvez pas réserver de trajets.")
        return redirect('home')
    
    trajet = get_object_or_404(Trajet, id=trajet_id)
    
    if trajet.passagers.filter(id=client_id).exists():
        messages.error(request, "Vous avez déjà réservé ce trajet.")
        return redirect('home')

    if trajet.est_complet():
        messages.error(request, "Ce trajet est complet. Il n'y a plus de places disponibles.")
        return redirect('home')
    
    if request.method == 'POST':
        trajet.passagers.add(client)
        trajet.nbPersonnes -= 1
        trajet.save()
        messages.success(request, "Vous avez réservé ce trajet avec succès.")
        return redirect('home')
    
    return render(request, 'trajet/rechercher.html', {'trajet': trajet})

def publier_trajet(request):
    client_id = request.session.get('client_id')
    if not client_id:
        return redirect('connexion')
    
    client = Client.objects.get(id=client_id)
    if not client.estConducteur:
        return redirect('error_not_conductor')

    if not client.is_active:
        messages.error(request, "Votre compte est suspendu. Vous ne pouvez pas publier de trajets.")
        return redirect('home')
 
    if not client.phone:
        messages.error(request, "Vous devez ajouter un numéro de téléphone à votre compte pour publier un trajet.")
        return redirect('compte')  
    
    if request.method == 'POST':
        form = TrajetForm(request.POST)
        if form.is_valid():
            trajet = form.save(commit=False)
            trajet.IDClientConducteur = client
            trajet.save()
            messages.success(request, "Trajet publié avec succès.")
            return redirect('home')
    else:
        form = TrajetForm()

    return render(request, 'trajet/publier_trajet.html', {'form': form})

def error_not_conductor(request):
    return render(request, 'trajet/error_not_conductor.html')

def changer_destination(request, trajet_id):
    trajet = get_object_or_404(Trajet, id=trajet_id)
    client_id = request.session.get('client_id')
    if not client_id or trajet.IDClientConducteur.id != client_id:
        return redirect('home')

    if request.method == 'POST':
        form = TrajetForm(request.POST, instance=trajet)
        if form.is_valid():
            form.save()
            messages.success(request, "La destination du trajet a été modifiée avec succès.")
            return redirect('mes_trajets')
    else:
        form = TrajetForm(instance=trajet)
    return render(request, 'trajet/changer_destination.html', {'form': form, 'trajet': trajet})

def annuler_trajet(request, trajet_id):
    trajet = get_object_or_404(Trajet, id=trajet_id)
    if trajet.IDClientConducteur.id == request.session.get('client_id'):
        if trajet.date - timezone.now().date() < timezone.timedelta(days=1):
            messages.error(request, "Vous ne pouvez pas annuler un trajet moins de 24 heures avant le départ.")
        else:
            trajet.delete()
            messages.success(request, "Le trajet a été annulé avec succès.")
    else:
        messages.error(request, "Vous n'êtes pas autorisé à annuler ce trajet.")
    return redirect('mes_trajets')

def modifier_trajet(request, trajet_id):
    trajet = get_object_or_404(Trajet, id=trajet_id)
    if trajet.IDClientConducteur.id != request.session.get('client_id'):
        messages.error(request, "Vous n'êtes pas autorisé à modifier ce trajet.")
        return redirect('mes_trajets')

    if request.method == 'POST':
        form = TrajetForm(request.POST, instance=trajet)
        if form.is_valid():
            form.save()
            messages.success(request, "Le trajet a été modifié avec succès.")
            return redirect('mes_trajets')
    else:
        form = TrajetForm(instance=trajet)
    return render(request, 'trajet/modifier_trajet.html', {'form': form})

def mes_trajets(request):
    client_id = request.session.get('client_id')
    trajets = Trajet.objects.filter(passagers=client_id) | Trajet.objects.filter(IDClientConducteur=client_id)
    context = {'trajets': trajets}
    return render(request, 'trajet/mes_trajets.html', context)

def annuler_reservation(request, trajet_id):
    trajet = get_object_or_404(Trajet, id=trajet_id)
    client_id = request.session.get('client_id')
    trajet.passagers.remove(client_id)
    messages.success(request, "Votre réservation a été annulée avec succès.")
    return redirect('mes_trajets')

