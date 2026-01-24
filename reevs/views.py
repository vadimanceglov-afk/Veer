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

    if request.method == "POST":
        #отримуємо дані з POST-запиту
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        capacity = request.POST.get("capacity")
        min_price = request.POST.get("min_price")
        max_price = request.POST.get("max_price")

        if start_date and end_date:
            #залишаємо вільні номери
            rooms = rooms.exclude(bookings__start_time__it = end_date, booking__end_time__gt = start_date)
            #враховуємо додаткові фільтри якщо вони вказані
            if capacity:
                rooms = rooms.filter(capacity__gte=capacity)
            if min_price:
                rooms = rooms.filter(min_price__gte=min_price)
            if max_price:
                rooms = rooms.filter(max_price__gte=max_price)   

        context = {
            "rooms": rooms,
            "start_date": start_date,
            "end_date": end_date,
            "min_price": min_price,
            "max_price": max_price,
            "capacity": capacity,
        }

    return render(request=request, template_name="rooms/main_page.html", context=context)

def book_room(request):
    if request.method == "GET":
        room_id = request.GET.get("room_id")
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        room = Room.objects.get(id = room_id)
        context = {
            "room": room,
            "start_date":start_date,
            "end_date":end_date
        }


        return render(request=request, template_name="rooms/booking.html", context=context)

    elif request.method == "POST":
        pass