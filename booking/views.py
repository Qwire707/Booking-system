from django.shortcuts import render, redirect
from .models import House, Client, Booking


def index(request):
    houses = House.objects.all()
    return render(request, "index.html", context={"houses": houses})

def house_detail(request, pk):
    house = House.objects.get(id=pk)
    return render(request, "house_detail.html", context={"house": house})

def booking_house(request, pk):
    if request.method == "GET":
        house = House.objects.get(id=pk)
        clients = Client.objects.all()
        context = {
            "house": house,
            "clients": clients,
        }
        return render(request, "booking_house.html", context=context)
    else:
        client_id = request.POST.get("client")
        arrival_date = request.POST.get("arrival_date")
        departure_date = request.POST.get("departure_date")
        comment = request.POST.get("comment")

        client = Client.objects.get(id=client_id)
        house = House.objects.get(id=pk)
        Booking.objects.create(
            client=client_id,
            house=house,
            arrival_date=arrival_date,
            departure_date=departure_date,
            comment=comment
        )
        return redirect("index")

