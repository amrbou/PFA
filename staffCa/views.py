from django.shortcuts import render, redirect, get_object_or_404
from .forms import StaffLoginForm
from .models import Staff
from trajet.models import Trajet
from client.models import Client
from trajet.forms import TrajetForm
from client.forms import ClientProfileForm


def staff_login(request):
    error_message = None
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                staff = Staff.objects.get(email=email)
                if staff.password == password:  # Simple password check
                    request.session['staff_id'] = staff.id
                    return redirect('admin_dashboard')  # Redirige vers un tableau de bord admin, à définir
                else:
                    error_message = "Email ou mot de passe incorrect"
            except Staff.DoesNotExist:
                error_message = "Email ou mot de passe incorrect"
    else:
        form = StaffLoginForm()
    return render(request, 'staffCa/staff_login.html', {'form': form, 'error_message': error_message})

def admin_dashboard(request):
    staff_id = request.session.get('staff_id')
    if not staff_id:
        return redirect('staff_login')

    trajets = Trajet.objects.all()
    clients = Client.objects.all()
    return render(request, 'staffCa/admin_dashboard.html', {'trajets': trajets, 'clients': clients})

def staff_logout(request):
    request.session.flush()
    return redirect('staff_login')

def modifier_trajet(request, trajet_id):
    staff_id = request.session.get('staff_id')
    if not staff_id:
        return redirect('staff_login')

    trajet = get_object_or_404(Trajet, id=trajet_id)
    if request.method == 'POST':
        form = TrajetForm(request.POST, instance=trajet)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = TrajetForm(instance=trajet)
    
    return render(request, 'staffCa/modifier_trajet.html', {'form': form, 'trajet': trajet})

def supprimer_trajet(request, trajet_id):
    staff_id = request.session.get('staff_id')
    if not staff_id:
        return redirect('staff_login')

    trajet = get_object_or_404(Trajet, id=trajet_id)
    if request.method == 'POST':
        trajet.delete()
        return redirect('admin_dashboard')

    return render(request, 'staffCa/supprimer_trajet.html', {'trajet': trajet})

def gerer_profil_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    trajets_conducteur = Trajet.objects.filter(IDClientConducteur=client)
    trajets_passager = client.trajets_passager.all() 
    if request.method == 'POST':
        estConducteur = request.POST.get('estConducteur') == 'on'
        client.estConducteur = estConducteur
        client.save()
        return redirect('admin_dashboard')
    return render(request, 'staffCa/gerer_profil_client.html', {
        'client': client,
        'trajets_conducteur': trajets_conducteur,
        'trajets_passager': trajets_passager
    })

def suspendre_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.is_active = not client.is_active
    client.save()
    return redirect('admin_dashboard')

def bannir_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return redirect('admin_dashboard')
