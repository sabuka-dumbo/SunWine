from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from datetime import datetime, timedelta
import re
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    print(Contact.objects.first().email)
    return render(request, "index.html", {
        "info": Indexpage.objects.all().get(id=1),
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
        "contacts": Contact.objects.first(),
        "gallery": Gallery.objects.all().first()
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
        country_code = request.POST.get('country')  # hidden input for code
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        # Combine into full phone number
        full_phone = f"{country_code}{phone_number}"

        if User.objects.filter(username=email).exists():
            print("Email already registered.")
            return redirect('register')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        user.first_name = full_name

        # Save phone number if field exists
        if hasattr(user, "phone_number"):
            user.phone_number = full_phone  

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

@login_required
def dashboard(request):
    return render(request, "dashboard.html", {
        "contacts": Contact.objects.first(),
        "room_count": Rooms.objects.all()
    })

def redirect_to_index(request, exception=None):
    return redirect('index')

handler404 = redirect_to_index

@login_required
def dashboard1(request):
    if request.method == "POST":
        room_id = request.POST.get("room")
        persons = request.POST.get("persons")
        check_in_str = request.POST.get("check-in")
        check_out_str = request.POST.get("check-out")
        comment = request.POST.get("comment", "")

        # Get room instance
        room = Rooms.objects.get(id=room_id)

        # Create check-in
        Check_In.objects.create(
            user=request.user,
            room=room,
            persons=persons,
            check_in=check_in_str,
            check_out=check_out_str,
            comment=comment,
        )

        return redirect("dashboard")

    rooms = Rooms.objects.all()
    return render(request, "your_template.html", {"room_count": rooms})

def room(request, roomid):
    if request.user.is_authenticated:
        if request.method == "POST":
            check_in_str = request.POST.get('check-in')
            check_out_str = request.POST.get('check-out')
            guests = request.POST.get('guests')

            try:
                check_in_date = datetime.strptime(check_in_str, '%Y-%m-%d').date()
                check_out_date = datetime.strptime(check_out_str, '%Y-%m-%d').date()
            except ValueError:
                return render(request, "room.html", {
                    "contacts": Contact.objects.first(),
                    "room": Rooms.objects.get(pk=roomid),
                    "error": "Invalid date format."
                })

            room = Rooms.objects.get(pk=roomid)
            user = request.user

            Check_In.objects.create(
                user=request.user,
                room=room,
                persons=guests,
                check_in=check_in_date,
                check_out=check_out_date
            )

            return redirect('bought')
        else:
            return render(request, "room.html", {
                "contacts": Contact.objects.first(),
                "room": Rooms.objects.get(pk=roomid),
            })
    else:
        return redirect('register') 

@login_required
def bought(request):
    return render(request, "bought.html")

def error_view(request, exception=None):
    return redirect('error')

def error(request):
    return render(request, "404.html")