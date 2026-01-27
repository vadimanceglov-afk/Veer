from django.shortcuts import render
from .models import Rest, Booking


#функція придставлення списку всіх кімнат
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
            rests = rests.exclude(bookings__start_time__it = end_date, booking__end_time__gt = start_date)
            #враховуємо додаткові фільтри якщо вони вказані
            if capacity:
                rests = rests.filter(capacity__gte=capacity)
            if min_price:
                rests = rests.filter(min_price__gte=min_price)
            if max_price:
                rests = rests.filter(max_price__gte=max_price)   

        context = {
            "rests": rests,
            "start_date": start_date,
            "end_date": end_date,
            "min_price": min_price,
            "max_price": max_price,
            "capacity": capacity,
        }

    return render(request=request, template_name="rests/main_page.html", context=context)


def book_rest(request):
    if request.method == "GET":
        rest_id = request.GET.get("rest_id")
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        rest = Rest.objects.get(id = rest_id)
        context = {
            "rest": rest,
            "start_date":start_date,
            "end_date":end_date
        }


        return render(request=request, template_name="rests/booking.html", context=context)

    elif request.method == "POST":
        pass