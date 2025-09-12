from django.shortcuts import render
from .models import HorseTour

def tour_list(request):
    tours = HorseTour.objects.all()
    return render(request, 'tours/tours_list.html', {'tours': tours})