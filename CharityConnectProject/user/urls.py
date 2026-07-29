from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("dashboard/", views.user_dashboard, name="dashboard"),
    path("profile/", views.profile_view, name="profile"),
    path("password/change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("logout/", views.logout_user, name="logout"),
]
