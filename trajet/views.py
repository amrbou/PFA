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
        return redirect('inscription')
    try:
        trajet = Trajet.objects.get(id=trajet_id)
        client = Client.objects.get(id=client_id)
        if client in trajet.passagers.all():
            messages.error(request, 'Vous avez déjà réservé ce trajet.')
        else:
            trajet.passagers.add(client)
            trajet.nbPersonnes += 1
            trajet.save()
            messages.success(request, 'Réservation effectuée avec succès.')
    except Trajet.DoesNotExist:
        messages.error(request, 'Le trajet n\'existe pas.')
    return redirect('recherche')


def publier_trajet(request):
    client_id = request.session.get('client_id')
    if not client_id:
        return redirect('connexion')

    client = get_object_or_404(Client, id=client_id)
    if not client.estConducteur:
        return redirect('error_not_conductor')  

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