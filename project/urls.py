"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('manager/',views.manager),
    path('employee/',views.employee),
    path('accounts/',include('django.contrib.auth.urls')),
    path('addemp/',views.addemp),
    path('empdata/',views.empdata),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
    path('select/',views.select),
    path('data/',views.getfile),
    path('addnews/',views.addnews),
    path('latestnews/',views.latestnews),
    path('addholiday/',views.addholiday),
    path('holycalender/',views.holycalender),
    
]
