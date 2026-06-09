from django.shortcuts import redirect, render
from . models import Room, Booking, User, Category


def home(request):
    rooms = Room.objects.all()
    
    
    return render(request, 'index.html', {'title': 'Головна сторінка',
                                          'rooms': rooms})
    
    
    
def booking_page(request, room_id):
    
    room = Room.objects.get(id=room_id)
    context = {"room":room}
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        check_in=request.POST.get("check_in")
        check_out=request.POST.get("check_out")
        
        booking = Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            room=room,
            check_in=check_in,
            check_out=check_out
            
            
            
        )
        return redirect('success')
        
       
        
    
    return render(request, 'book.html', context)


def success(request):
    return render(request, 'suscfull.html')
    room = Room.objects.get(id=room_id)
    context = {"room":room}
    return render(request, 'book.html', context)

    
    


