
from django.contrib.auth import views as auth_views
from Proyecto.views import CustomLoginView
from Proyecto.views import LoginForm
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('Proyecto.urls')),
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='Proyecto/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Proyecto/logout.html'), name='logout'),
]