from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/<int:room_id>/',views.booking_page, name='book_page' )
]