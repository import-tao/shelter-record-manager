from django.urls import path
from . import views
from .views import AnimalDetailView


urlpatterns = [
    path('', views.homepage, name='home_page'),
    path('<name>/<id>/', AnimalDetailView.as_view() , name='animal_detail'),
]