from django.shortcuts import render

def index(request):
    return render(request, 'site_projeto/index.html')
