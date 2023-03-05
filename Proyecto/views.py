from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView

#Pagina de Inicio
def home(request):
    return render(request, 'Proyecto/home.html')

#Registro y Logueo
class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'Proyecto/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario {username} creado')

            return redirect(to='/')
        
class CustomLoginView(LoginView):
    form_class= LoginForm
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(CustomLoginView, self).form.valid(form)

def dispatch(self, request, *args, **kwargs):
        # se redirigirá a la página de inicio si un usuario intenta acceder a la página de registro mientras está conectado
        if request.user.is_authenticated:
            return redirect(to='/')

        # de lo contrario, procese el envío como lo haría normalmente
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
    
    