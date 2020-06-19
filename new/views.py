from django.shortcuts import render
from django.http import HttpResponse
from .models import NewClass


def new(request):
    items = NewClass.objects.all()
    return render(request, 'new.html', items='allItems')

