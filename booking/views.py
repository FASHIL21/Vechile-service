from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Booking

def home(request):
    return render(request, 'home.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'profile.html', {'bookings': bookings})

@login_required
def book_service(request):
    if request.method == 'POST':
        Booking.objects.create(
            user=request.user,
            vehicle_no=request.POST['vehicle_no'],
            service_type=request.POST['service_type'],
            booking_date=request.POST['booking_date'],
            booking_time=request.POST['booking_time']
        )
        return redirect('profile')
    return render(request, 'book.html')

@login_required
def admin_panel(request):
    if not request.user.is_staff:
        return redirect('home')
    data = Booking.objects.all()
    return render(request, 'admin_panel.html', {'data': data})

