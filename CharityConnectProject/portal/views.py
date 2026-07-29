from django.shortcuts import render

def home(request):
    return render(request, "portal/home.html")

def about(request):
    return render(request, "portal/about.html")

def services(request):
    return render(request, "portal/services.html")

def gallery(request):
    return render(request, "portal/gallery.html")