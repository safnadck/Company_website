from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')


def services(request):
    return render(request, 'main/services.html')

def team(request):
    return render(request, 'main/team.html')


def contact(request):
    return render(request, 'main/contact.html')