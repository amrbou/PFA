from django.shortcuts import render, redirect
from django.contrib.auth import logout
from client.models import Client
from client.forms import InscriptionForm, ConnexionForm, CompteForm
from trajet.models import Trajet


def home(request):
    client_id = request.session.get('client_id')
    context = {'client_id': client_id}
    return render(request, 'client/home.html', context)

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            Client.objects.create(nom=nom, password=password, email=email)
            return redirect('home')
    else:
        form = InscriptionForm()
    return render(request, 'client/inscription.html', {'form': form})

def index(request):
    return render(request, 'client/index.html')

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                client = Client.objects.get(email=email)
                if password == client.password:  
                    request.session['client_id'] = client.id  
                    return redirect('home')
                else:
                    form.add_error(None, "Email ou mot de passe incorrect")
            except Client.DoesNotExist:
                form.add_error(None, "Email ou mot de passe incorrect")
    else:
        form = ConnexionForm()
    return render(request, 'client/connexion.html', {'form': form})

def deconnexion(request):
    request.session.flush()
    return redirect('home')

def compte(request):
    client_id = request.session.get('client_id')
    if not client_id:
        return redirect('connexion')
    
    client = Client.objects.get(id=client_id)
    error_message = None

    if request.method == 'POST':
        form = CompteForm(request.POST, request.FILES, instance=client)
        current_password = request.POST.get('current_password')

        if current_password != client.password:
            error_message = "Mot de passe actuel incorrect"
        elif form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CompteForm(instance=client)
    
    return render(request, 'client/compte.html', {'form': form, 'error_message': error_message})

def mes_trajets(request):
    client_id = request.session.get('client_id')
    if not client_id:
        return redirect('connexion')
    
    trajets = Trajet.objects.filter(passagers=client_id)
    return render(request, 'client/mes_trajets.html', {'trajets': trajets})
