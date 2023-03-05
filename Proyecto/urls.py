from django.urls import path
from Proyecto.views import home, RegisterView
from Proyecto import views

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('clientes/', views.clientes, name="registrar-cliente"),
    path('planes/', views.planes, name="planes"),
    path('buscar/', views.buscar),
]