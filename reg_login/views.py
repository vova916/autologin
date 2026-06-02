from django.shortcuts import render
from . models import Room, Booking, User, Category


def home(request):
    rooms = Room.objects.all()
    
    
    return render(request, 'index.html', {'title': 'Головна сторінка',
                                          'rooms': rooms})
    
    
    
def booking_page(request, room_id):
    
    room = Room.objects.get(id=room_id)
    context = {"room":room}
    
    return render(request, 'book.html', context)
    


