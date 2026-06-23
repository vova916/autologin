from django.shortcuts import redirect, render
from . models import Room, Booking, User, Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    rooms = Room.objects.all()
    
    capacity = request.GET.get('capacity')
    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')
    
    if capacity:
        rooms = rooms.filter(capacity__gte=capacity)
    if check_in and check_out: 
        rooms = rooms.exclude(bookings__check_in__lt=check_out, bookings__check_out__gt=check_in)
    
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
        
        
        
        exiting_bookings = Booking.objects.filter(room=room, check_in__lt=check_out, check_out__gt = check_in )
        if exiting_bookings.exists():
            messages.error(request, "На обрані дати апартаменти вже забронювані ")
            return redirect('book_page',room_id=room.id)
        else: 
        
            booking = Booking.objects.create(
                name=name,
                email=email,
                phone=phone,
                room=room,
                check_in=check_in,
                check_out=check_out,
                customer=request.user if request.user.is_authenticated else None
            )
            return redirect('success')
        
       
        
    
    return render(request, 'book.html', context)


def success(request):
    return render(request, 'suscfull.html')
    room = Room.objects.get(id=room_id)
    context = {"room":room}
    return render(request, 'book.html', context)


@login_required
def user_booking(request):
    bookings = Booking.objects.filter(customer=request.user)
    context = {"bookings": bookings}
    
    return render(request, 'user_booking.html', context)
