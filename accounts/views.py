from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from dashboard.models import Farmer


class ShetiMitraLoginView(LoginView):

    template_name = 'accounts/login.html'

    redirect_authenticated_user = False

    next_page = '/'


class ShetiMitraLogoutView(LogoutView):

    next_page = '/login/'


def register(request):

    if request.method == "POST":

        # Registration form data
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        village = request.POST.get("village")
        taluka = request.POST.get("taluka")
        district = request.POST.get("district")
        land_area_acres = request.POST.get("land_area_acres")

        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Password match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        # Create User
        user = User.objects.create_user(
            username=username,
            password=password
        )

        # Create Farmer profile
        Farmer.objects.create(
            user=user,
            name=name,
            mobile=mobile,
            village=village,
            taluka=taluka,
            district=district,
            land_area_acres=land_area_acres
        )

        messages.success(
            request,
            "Registration successful. Please login."
        )

        return redirect("login")

    return render(
        request,
        "accounts/register.html"
    )