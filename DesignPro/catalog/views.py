from django.shortcuts import render
from .forms import UserLoginForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')


class Login(FormView):
    template_name = 'catalog/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # Аутентификация пользователя
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Неправильное имя пользователя или пароль.')
            return self.form_invalid(form)