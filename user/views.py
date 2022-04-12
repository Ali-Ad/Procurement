from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render


class CustomLoginView(LoginView):
    template_name = 'account/login.html'


@login_required
def Home(request):
    return render(request, 'account/home.html')
