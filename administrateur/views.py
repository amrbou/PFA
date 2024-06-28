# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from administrateur.models import Administrateur
from .forms import AdminConnexionForm

def admin_connexion(request):
    if request.method == 'POST':
        form = AdminConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['emailAdmin']
            password = form.cleaned_data['password']
            try:
                admin = Administrateur.objects.get(emailAdmin=email)
                if check_password(password, admin.password):
                    request.session['admin_id'] = admin.id
                    return redirect('verification_permis')
                else:
                    form.add_error(None, "Email ou mot de passe incorrect")
            except Administrateur.DoesNotExist:
                form.add_error(None, "Email ou mot de passe incorrect")
    else:
        form = AdminConnexionForm()
    return render(request, 'staff_login.html', {'form': form})
