import random

from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


def get_new_password():
    password_base = "abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    password_base_list = list(password_base)
    abrakadabra = random.sample(password_base_list, 10)
    new_password = ''.join(abrakadabra)
    return new_password


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register_form.html'


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    template_name = 'users/profile_form.html'

    def get_object(self, queryset=None):
        return self.request.user


def confirm_email(request, token):
    user = User.objects.get(verification_code=token)
    if user is None:
        return render(request, 'users/register.html', {'title': 'Неудачная попытка подтверждения почты'})
    else:
        user.is_active = True
        user.verification_code = ''
        user.save()
        return render(request, 'users/confirm_email.html')


def forgot_pass_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.get(email=email)
        if user:
            password = get_new_password()
            res = send_mail('Новый пароль',
                            f"Ваш новый пароль: { password }",
                            'skyprothebest@mail.ru',
                            [email])
            user.set_password(password)
            user.save()
            return render(request, 'users/reset_pass_form_success.html', {'title': 'Пароль сброшен'})
    else:
        return render(request, 'users/reset_pass_form.html')