from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import RegisterForm, LoginForm, ClienteFormulario
from .models import Cliente, Plan
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from Proyecto.models import *
from Proyecto.forms import *

#Pagina de Inicio
def home(request):
    return render(request, 'Proyecto/home.html')

def planes(request):
      return render(request, "Proyecto/planes.html")

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
    
#Registrar Cliente
def clientes(request):
      if request.method == 'POST':
            miFormulario = ClienteFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid():   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  cliente = Cliente (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email']) 
                  cliente.save()
                  return render(request, "Proyecto/clientes.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= ClienteFormulario() #Formulario vacio para construir el html
      return render(request, "Proyecto/clientes.html", {"miFormulario":miFormulario})

#Buscar Plan
def buscar(request):
      if request.GET["numero"]:
            numero = request.GET['numero'] 
            planes = Plan.objects.filter(numero__icontains=numero)
            return render(request, "Proyecto/planes.html", {"planes":planes, "numero":numero})
      else: 
            respuesta = "No enviaste datos"
      return render(request, "Proyecto/planes.html", {"respuesta":respuesta})
