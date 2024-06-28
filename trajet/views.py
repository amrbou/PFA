from django.shortcuts import render, redirect, get_object_or_404
from trajet.models import Trajet
from trajet.forms import RechercheForm
from .forms import TrajetForm
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
    if request.method == 'POST':
        trajet.passagers.add(client)
        trajet.nbPersonnes += 1
        trajet.save()
        messages.success(request, "Vous avez réservé ce trajet avec succès.")
        return redirect('mes_trajets')
    
    return render(request, 'trajet/reserver.html', {'trajet': trajet})


def publier_trajet(request):
    client_id = request.session.get('client_id')
    if not client_id:
        return redirect('connexion')
    
    client = Client.objects.get(id=client_id)
    if not client.is_active:
        messages.error(request, "Votre compte est suspendu. Vous ne pouvez pas publier de trajets.")
        return redirect('home')

    if request.method == 'POST':
        form = TrajetForm(request.POST)
        if form.is_valid():
            trajet = form.save(commit=False)
            trajet.IDClientConducteur = client
            trajet.save()
            return redirect('home')
    else:
        form = TrajetForm()

    return render(request, 'trajet/publier_trajet.html', {'form': form})

def error_not_conductor(request):
    return render(request, 'trajet/error_not_conductor.html')