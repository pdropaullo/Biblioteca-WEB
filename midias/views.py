from django.shortcuts import render
from . models import Midias


def index(request):
    midias = Midias.objects.all()
    return render(request, 'pages/index.html', {'midias': midias})


def search(request):
    q = request.GET.get('search')
    midias = Midias.objects.filter(title__icontains=q)
    return render(request, 'pages/index.html', {'midias': midias})