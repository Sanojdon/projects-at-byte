from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'accounts/index.html')

def details(request):
    print(request)
    return render(request, 'accounts/details.html')
