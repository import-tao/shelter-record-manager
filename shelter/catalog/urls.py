from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home_page'),
    path('create/', views.AnimalCreateView, name="animal_create"),
    path('<name>/<int:pk>/', views.AnimalDetailView.as_view(), name='animal_detail'),
    path('<name>/<int:pk>/update/', views.AnimalInstanceUpdateView.as_view(), name= "animal_instance_update"),
    path('<name>/<int:pk>/update/animal', views.AnimalTypeUpdateView.as_view(), name= 'animal_type_update'),
    path('<name>/<int:pk>/delete', views.AnimalInstanceDeleteView.as_view(), name= 'animal_instance_delete'),
]