from django.shortcuts import render
from . models import Room, Booking, User, Category


def home(request):
    rooms = Room.objects.all()
    
    
    return render(request, 'index.html', {'title': 'Головна сторінка',
                                          'rooms': rooms})


