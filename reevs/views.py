from django.shortcuts import render
from .models import Room, Booking


#функція придставлення списку всіх кімнат
def rooms_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms
    }
    return render(request=request, template_name="places/room_list.html", context=context)