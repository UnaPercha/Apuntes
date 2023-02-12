"""primerProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from primerProyecto import views #importamos el archivo views en el que se encuentra la vista de la página

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo, name='saludo'), #indicamos la url de la función en views como 'saludo/'(no es necesario que se llame igual que la función pero es recomendable),
                                                #luego le indicamos la función que se encuentra en views y finalmente como queremos que se llame con name='nombre' aunque esto ultimo es opcional
                                                #para verlo el archivo se encontrará en la url indicada en runserver seguida de /saludo/. por ejemplo http://127.0.0.1:8000/saludo/
    path('byebye/', views.byebye, name='byebye')
]
