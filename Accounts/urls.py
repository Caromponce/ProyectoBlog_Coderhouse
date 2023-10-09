from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_request, name="Login"),
    path('logout', views.logout_request, name="Logout"),
    path('register', views.register, name="Register"),
    path('profile', views.profile, name="Profile"),
    path('editProfile', views.edit_profile, name="Edit_profile"),
    path('changePassword', views.change_password, name="Change_password")
]
