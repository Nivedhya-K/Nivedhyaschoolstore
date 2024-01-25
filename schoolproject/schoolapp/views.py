from django.shortcuts import render

from schoolapp import views

def home(request):
    return render(request, "home.html")

