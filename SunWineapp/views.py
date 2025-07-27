from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Q
from datetime import datetime, timedelta
import re


# Create your views here.
def index(request):
    print(Contact.objects.first().email)
    return render(request, "index.html", {
        "contacts": Contact.objects.first()
    })

def services(request):
    return render(request, "services.html", {
        "contacts": Contact.objects.first(),
        "service1": Services.objects.all().get(service_title="Relaxation & Leisure Areas"),
        "service2": Services.objects.all().get(service_title="Comfortable Rooms with Daily Housekeeping"),
        "service3": Services.objects.all().get(service_title="Guest Convenience Services"),
    })

def gallery(request):
    return render(request, "gallery.html", {
        "contacts": Contact.objects.first()
    })

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        
        if not User.objects.filter(username=email).exists():
            print("User does not exist.")
        else:
            print("User found, trying to authenticate...")

        if user is not None:
            login(request, user)
            print("Login successful.")
            return redirect('booking')
        else:
            print("Invalid email or password.")
            return redirect('login')

    return render(request, 'login.html', {
        "contacts": Contact.objects.first()
    })

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')

        if User.objects.filter(username=email).exists():
            print("Email already registered.")
            return redirect('register')

        user = User.objects.create_user(username=email, phone_number=phone_number, full_name=full_name, email=email, password=password)
        user.first_name = full_name
        user.save()

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print("Account created and logged in successfully.")
            return redirect('booking')
        else:
            print("Authentication failed after registration.")
            return redirect('login')

    return render(request, 'register.html', {
        "contacts": Contact.objects.first()
    })

def booking(request):
    if not request.user.is_authenticated:
        return redirect('register')

    message = ""
    results = ''

    today = datetime.today().date()
    next_week = today + timedelta(days=7)

    candidate_rooms_next7 = Rooms.objects.filter(available=True)

    conflicting_next7 = Check_In.objects.filter(
        Q(check_in__lt=next_week) & Q(check_out__gt=today)
    ).values_list('room_id', flat=True)

    available_next_7_days = candidate_rooms_next7.exclude(id__in=conflicting_next7)

    if request.method == "POST":
        check_in_str = request.POST.get('check-in')
        check_out_str = request.POST.get('check-out')
        guests_str = request.POST.get('guests')

        try:
            check_in = datetime.strptime(check_in_str, "%Y-%m-%d").date()
            check_out = datetime.strptime(check_out_str, "%Y-%m-%d").date()

            if check_in >= check_out:
                message = "Check-out date must be after check-in date."
            else:
                guest_numbers = list(map(int, re.findall(r'\d+', guests_str)))
                guests_total = sum(guest_numbers)

                candidate_rooms = Rooms.objects.filter(available=True, bed__gte=guests_total)

                conflicting_bookings = Check_In.objects.filter(
                    Q(check_in__lt=check_out) & Q(check_out__gt=check_in)
                ).values_list('room_id', flat=True)

                available_rooms = candidate_rooms.exclude(id__in=conflicting_bookings)

                if not available_rooms.exists():
                    message = "No rooms available for the selected dates."

                results = available_rooms

        except (ValueError, TypeError):
            message = "Please enter valid dates and select guests."

    return render(request, "booking.html", {
        "results": results,
        "contacts": Contact.objects.first(),
        "message": message,
        "rooms2": available_next_7_days
    })

def dashboard(request):
    return render(request, "dashboard.html", {
        "contacts": Contact.objects.first()
    })

def room(request, roomid):
    if request.method == "POST":
        return redirect('index')
    else:
        return render(request, "room.html", {
            "contacts": Contact.objects.first(),
            "room": Rooms.objects.all().get(pk=roomid),
        })