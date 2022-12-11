from django.shortcuts import render
from django.template import loader

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def about_me(request):
    return render(request, 'about_me.html', {})


def my_projects(request):
    return render(request, 'projects-menu.html', {})