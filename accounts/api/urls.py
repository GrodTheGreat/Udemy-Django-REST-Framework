from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path(route="login/", view=obtain_auth_token, name="login"),
    path(route="logout/", view=views.logout_view, name="logout"),
    path(route="register/", view=views.registration_view, name="register"),
]
