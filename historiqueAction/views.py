from django.shortcuts import render, redirect, get_object_or_404
from .models import HistoriqueAction
from client.models import Client
from trajet.forms import TrajetForm
from django.contrib import messages
from trajet.models import Trajet

def historique_action(request):
    client_id = request.session.get('client_id')
    if not client_id:
        return redirect('connexion')

    historique_actions = HistoriqueAction.objects.filter(client_id=client_id).order_by('-created_at')
    return render(request, 'historique_action.html', {'historique_actions': historique_actions})

def modifier_trajet(request, trajet_id):
    trajet = get_object_or_404(Trajet, id=trajet_id)
    if request.method == 'POST':
        form = TrajetForm(request.POST, instance=trajet)
        if form.is_valid():
            form.save()
            HistoriqueAction.objects.create(
                client=trajet.IDClientConducteur,
                message=f'Votre trajet de {trajet.pointDepart} à {trajet.pointArrivee} a été modifié.'
            )
            for passager in trajet.passagers.all():
                HistoriqueAction.objects.create(
                    client=passager,
                    message=f'Le trajet de {trajet.pointDepart} à {trajet.pointArrivee} auquel vous participez a été modifié.'
                )
            messages.success(request, "Le trajet a été modifié avec succès.")
            return redirect('mes_trajets')
    else:
        form = TrajetForm(instance=trajet)
    return render(request, 'trajet/modifier_trajet.html', {'form': form})

def suspendre_utilisateur(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.is_active = False
    client.save()
    HistoriqueAction.objects.create(
        client=client,
        message='Votre compte a été suspendu par un administrateur.'
    )
    messages.success(request, f"L'utilisateur {client.nom} a été suspendu.")
    return redirect('admin_dashboard')
