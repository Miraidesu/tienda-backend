"""
URL configuration for tienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from .views import LoginView, login_html_view, logout_html_view

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.index, name='index'),
	path('login/', views.login_html_view, name='login_html_view'),
	path('logout/', views.logout_html_view, name='logout_html_view'),
	path('componentes/<int:id>', views.detalle_componente, name='detalle_componente'),
	path('componentes/', views.lista_componentes, name='lista_componentes'),
	path('carrito/', views.carrito_compras, name='carrito_compras'),
	path('carrito/agregar/<int:id>', views.agregar_carrito, name='agregar_carrito'),
	path('pagar', views.pagar, name='pagar'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


