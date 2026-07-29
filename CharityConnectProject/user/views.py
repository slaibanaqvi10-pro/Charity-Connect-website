from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required




# -----------------------------
# REGISTER USER (Simple)
# -----------------------------
def register_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        volunteer_program = request.POST.get("volunteer_work")  # frontend se volunteer_work input

        # Password check
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        # Email duplicate check
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered!")
            return redirect("register")

        # Create User
        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=name,
            password=password
        )

        # Save Profile
        UserProfile.objects.create(
            user=user,
            volunteer_program=volunteer_program
        )

        messages.success(request, "Account created successfully! Please login.")
        return redirect("login")

    return render(request, "user/register.html")


# -----------------------------
# LOGIN USER
# -----------------------------
def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=email, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid email or password!")
            return redirect("login")

    return render(request, "user/login.html")


# -----------------------------
# USER DASHBOARD
# -----------------------------
@login_required
def user_dashboard(request):
    # Get or create profile for current user
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    context = {
        "name": request.user.first_name,
        "email": request.user.email,
        "volunteer": profile.volunteer_program,   # <-- Fixed
        "date": profile.created_at if hasattr(profile, "created_at") else "",
    }

    return render(request, "user/dashboard.html", context)


# -----------------------------
# PROFILE VIEW + UPDATE
# -----------------------------
@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile.full_name = request.POST.get("full_name")
        profile.father_name = request.POST.get("father_name")
        profile.phone = request.POST.get("phone")
        profile.address = request.POST.get("address")
        profile.dob = request.POST.get("dob")
        profile.age = request.POST.get("age")
        profile.nationality = request.POST.get("nationality")
        # profile.occupation = request.POST.get("occupation")  # remove this line
        profile.marital_status = request.POST.get("marital_status")
        profile.save()

        messages.success(request, "Profile updated successfully!")
        return redirect("profile")

    return render(request, "user/profile.html", {"profile": profile})
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out successfully!")
    return redirect("login")
