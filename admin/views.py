from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import AdminInscriptionForm, AdminConnexionForm
from .models import Admin

def admin_inscription(request):
    if request.method == 'POST':
        form = AdminInscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            admin = Admin.objects.create_user(email=email, password=password)
            return redirect('admin_connexion')
    else:
        form = AdminInscriptionForm()
    return render(request, 'admin/admin_inscription.html', {'form': form})

def admin_connexion(request):
    if request.method == 'POST':
        form = AdminConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            admin = authenticate(request, email=email, password=password)
            if admin is not None:
                login(request, admin)
                return redirect('verification_permis')
            else:
                form.add_error(None, "Email ou mot de passe incorrect")
    else:
        form = AdminConnexionForm()
    return render(request, 'admin/admin_connexion.html', {'form': form})
