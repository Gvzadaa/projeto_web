from django.shortcuts import render


# Create your views here.

def institucional(request):
    return render(request, 'site_institucional/index.html')


