from django.shortcuts import render
from .models import Room, Booking


#функція придставлення списку всіх кімнат
def rooms_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms
    }
    return render(request=request, template_name="rooms/room_list.html", context=context)

def main_page(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
        "start_date": "",
        "end_date": "",
        "min_price": "",
        "max_price": "",
        "capacity": "",
    }

    return render(request=request, template_name="rooms/main_page.html", context=context)