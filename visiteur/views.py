from django.shortcuts import render
from django.http import HttpResponse
from .models import Visiteur

def inscription(request):
    if request.method == 'POST':
        pass
    return render(request, 'visiteur/inscription.html')
def example(request):
    return HttpResponse("This is an example view.")