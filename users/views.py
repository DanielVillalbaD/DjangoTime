from django.contrib import messages
from django.contrib.auth import authenticate, login as dlogin, logout as dlogout
from django.shortcuts import render, redirect
from django.views import View

from users.forms import NewUserForm, LoginForm


class LoginView(View):

    def get(self, request):

        form = LoginForm()
        context = {'form': form}

        return render(request, 'forms/login.html', context)

    def post(self, request):

        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, 'Usuario o contraseña incorrectos')
            else:
                dlogin(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)

        form = LoginForm()

        context = {'form': form}
        return render(request, 'forms/login.html', context)

class LogoutView(View):

    def get(self, request):
        """
        Hace logout del usuario y redirige al login.html
        :param request: HttpRequest
        :return: HttpResponse y redirect a login.html
        """
        dlogout(request)
        return redirect('login.html')

class CreateUserView(View):

    def get(self, request):
        """
        Presenta el formulario de creación de un usuario
        :param request: objeto HttpRequest
        :return: HttpResponse con respuesta
        """

        form = NewUserForm()

        context = {'form': form}
        return render(request, 'forms/sign-up.html', context)

    def post(self, request):
        """
        Procesa el formulario de creación de un usuario
        :param request: objeto HttpRequest
        :return: HttpResponse con respuesta
        """

        form = NewUserForm(request.POST)

        if form.is_valid():
            sign_up = form.save()

        form = NewUserForm()
        messages.success(request, '¡Usuario Creado! Puedes comenzar a publicar')
        context = {'form': form}
        return render(request, 'forms/sign-up.html', context)