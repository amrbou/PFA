from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'client/home.html')
def inscription(request):
    return HttpResponse("Page d'inscription")
def index(request):
    return HttpResponse("Hello, this is the client app.")
