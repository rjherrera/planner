from django.shortcuts import render
from .utils import malla


def home(request):
    return render(request, 'home.html', {'malla': malla})
