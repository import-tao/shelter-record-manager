"""shelter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include
from . import views

# The include function means for anythin which is 'app/' in the url, it will send it to the catalog app, urls file
# The next step of routing is then handled by the urls.py file in catalog/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    # Naming the paths make it a lot easier for front end and particularly when make changes
    path('', views.index, name= 'index'),
    path('app/', include('catalog.urls'))
]
