from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view, name='home_page'),
    path('adopted/', views.adopted_animals_view, name='adopted_animals'),
    path('create/', views.AnimalCreateView, name="animal_create"),
    path('<name>/<int:pk>/', views.AnimalDetailView.as_view(), name='animal_detail'),
    path('<name>/<int:pk>/update/', views.AnimalInstanceUpdateView.as_view(), name= "animal_instance_update"),
    path('<name>/<int:pk>/update/animal', views.AnimalTypeUpdateView.as_view(), name= 'animal_type_update'),
    path('<name>/<int:pk>/delete', views.AnimalInstanceDeleteView.as_view(), name= 'animal_instance_delete'),
    path('adopt/<name>/<int:pk>/', views.animalinstanceadoptview, name = 'adopt_new'),
    path('cage/', views.cagedetailview, name='cage_detail'),
    path('cage/create/', views.cagecreateview, name='cage_create'),
    path('cage/<room>/<int:pk>/', views.CageUpdateView.as_view(), name='cage_update'),
    path('cage/<room>/<int:pk>/delete/', views.CageDeleteView.as_view(), name='cage_delete'),
]