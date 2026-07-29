from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('donate_now', views.donate, name='donate'),
    path('donation_success/', views.donation_success, name='donation_success'),
    path('user/', include('user.urls')),  # Include user app URLs
    path('campaign_list/', views.campaign_list, name='campaign_list'),

    path("admin/", admin.site.urls),

    path("accounts/", include("django.contrib.auth.urls")),  # 🔥 add this
    path("", include("portal.url")),
    path("user/", include("user.urls")),
path("accounts/", include("django.contrib.auth.urls")),


]


