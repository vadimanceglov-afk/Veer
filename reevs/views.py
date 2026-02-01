from django.shortcuts import render
from .models import Rest, Booking, Room
from django.db.models import Q
from datetime import datetime

# функція придставлення списку всіх кімнат
def rests_list(request):
    rests = Rest.objects.all()
    context = {
        "rests": rests
    }
    return render(request=request, template_name="rests/rests_list.html", context=context)

def sef(request):
    return render(request=request, template_name="rests/sef.html")

def main_page(request):
    rests = Rest.objects.all()
    context = {
        "rests": rests,
        "start_date": "",
        "end_date": "",
        "min_price": "",
        "max_price": "",
        "capacity": "",
        "tep": "",
    }

    if request.method == "POST":
        # отримуємо дані з POST-запиту
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        capacity = request.POST.get("capacity")
        tep = request.POST.get("tep")
        min_price = request.POST.get("min_price")
        max_price = request.POST.get("max_price")

        if start_date and end_date:
            # конвертуємо дати у datetime.date
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

            # залишаємо вільні номери
            rests = rests.exclude(
                rooms__bookings__start_time__lt=end_date,
                rooms__bookings__end_time__gt=start_date
            )

            # враховуємо додаткові фільтри якщо вони вказані
            if capacity:
                rests = rests.filter(rooms__capacity__gte=capacity).distinct()
            if min_price:
                rests = rests.filter(price__gte=min_price)
            if max_price:
                rests = rests.filter(price__lte=max_price)
            if tep:
                rests = rests.filter(tep=tep)

        context = {
            "rests": rests,
            "start_date": start_date,
            "end_date": end_date,
            "min_price": min_price,
            "max_price": max_price,
            "capacity": capacity,
            "tep": tep,
        }

    return render(request=request, template_name="rests/main_page.html", context=context)


def book_rest(request):
    if request.method == "GET":
        room_id = request.GET.get("room_id")
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        room = Room.objects.get(id=room_id)

        context = {
            "room": room,
            "start_date": start_date,
            "end_date": end_date
        }

        return render(request, "rests/booking.html", context)

    elif request.method == "POST":
        room_id = request.POST.get("room_id")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        guests_count = request.POST.get("guests_count", 1)

        room = Room.objects.get(id=room_id)

        # конвертуємо дати у datetime.date
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        context = {
            "room": room,
            "start_date": start_date,
            "end_date": end_date
        }

        # перевіряємо коректність дат
        if start_date > end_date:
            return render(request=request, template_name="rests/booking.html", context=context)
        
        # перевіряємо чи цей номер уже заброньований кимось
        if Booking.objects.filter(room=room, start_time__lt=end_date, end_time__gt=start_date).exists():
            return render(request=request, template_name="rests/booking.html", context=context)

        # створюємо нове бронювання
        booking = Booking.objects.create(
            user=request.user,
            room=room,
            start_time=start_date,
            end_time=end_date,
            guests_count=guests_count
        )

        return render(request=request, template_name="rests/success.html", context={"booking": booking})
