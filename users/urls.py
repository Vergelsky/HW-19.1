from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, confirm_email, forgot_pass_view

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='users/login.html'), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('confirm_email/<token>/', confirm_email, name='confirm_email'),
    path('forgot', forgot_pass_view, name='forgot'),
]