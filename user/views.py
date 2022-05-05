from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from axes.decorators import axes_dispatch
from django.views.generic import TemplateView

from . import forms


class CustomLoginView(LoginView):
    template_name = 'account/login.html'


def register(request):
    form = forms.CreateUserForm()
    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html', context)


@login_required
def Home(request):
    return render(request, 'account/home.html')


class ChangePasswordView(PasswordChangeView):
    template_name = 'account/change_password.html'
    success_url = reverse_lazy('home')


class CustomerLogout(LogoutView):
    success_url = reverse_lazy('login')


class Lock(TemplateView):
    template_name = 'account/lock.html'
