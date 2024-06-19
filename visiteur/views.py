from django.http import HttpResponse
from django.shortcuts import render, redirect

def example(request):
    return HttpResponse("This is an example view.")