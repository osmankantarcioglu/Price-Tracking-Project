from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CruiseAlert
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

SHIP_CHOICES = [
    "Adventure of the Seas",
    "Allure of the Seas",
    "Anthem of the Seas",
    "Brilliance of the Seas",
    "Enchantment of the Seas",
    "Explorer of the Seas",
    "Freedom of the Seas",
    "Grandeur of the Seas",
    "Harmony of the Seas",
    "Icon of the Seas",
    "Independence of the Seas",
    "Jewel of the Seas",
    "Legend of the Seas",
    "Liberty of the Seas",
    "Mariner of the Seas",
    "Navigator of the Seas",
    "Oasis of the Seas",
    "Odyssey of the Seas",
    "Ovation of the Seas",
    "Quantum of the Seas",
    "Radiance of the Seas",
    "Rhapsody of the Seas",
    "Serenade of the Seas",
    "Spectrum of the Seas",
    "Star of the Seas",
    "Symphony of the Seas",
    "Utopia of the Seas",
    "Vision of the Seas",
    "Voyager of the Seas",
    "Wonder of the Seas",
]

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    created = False
    if request.method == 'POST':
        if 'delete_alert' in request.POST:
            alert_id = request.POST.get('delete_alert')
            alert = get_object_or_404(CruiseAlert, id=alert_id, user=request.user)
            alert.delete()
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            ship_name = request.POST.get('ship_name')
            sail_date = request.POST.get('sail_date')
            purchase_price = request.POST.get('purchase_price')
            purchase_type = request.POST.get('purchase_type')
            if ship_name and sail_date and purchase_price and purchase_type:
                CruiseAlert.objects.create(
                    user=request.user,
                    ship_name=ship_name,
                    sail_date=sail_date,
                    purchase_price=purchase_price,
                    purchase_type=purchase_type,
                )
                return HttpResponseRedirect(reverse('dashboard'))
    alerts = CruiseAlert.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'accounts/dashboard.html', {
        'alerts': alerts,
        'ship_choices': SHIP_CHOICES,
        'created': created,
    })
