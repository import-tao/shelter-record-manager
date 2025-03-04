from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view, name='home_page'),
    # list of animals
    path('available/', views.available_animals_view, name='available_animals'),
    path('adopted/', views.adopted_animals_view, name='adopted_animals'),
    path('reserved/', views.reserved_animals_view, name='reserved_animals'),
    path('quarantine/', views.quarantined_animals_view, name='quarantined_animals'),

    path('create/', views.AnimalCreateView.as_view(), name="animal_create"),
    path('<int:pk>/', views.AnimalDetailView.as_view(), name='animal_detail'),
    path('<int:pk>/update/', views.AnimalInstanceUpdateView.as_view(), name= "animal_instance_update"),
    path('<int:pk>/delete/', views.AnimalInstanceDeleteView.as_view(), name= 'animal_instance_delete'),
    path('adopt/<int:pk>/', views.animalinstanceadoptview, name = 'adopt_new'),
    path('adopted/<int:pk>/', views.animalinstanceadoptview, name= 'adopt_existing'),
    path('cage/', views.cagedetailview, name='cage_detail'),
    path('cage/create/', views.cagecreateview, name='cage_create'),
    path('cage/<int:pk>/', views.CageUpdateView.as_view(), name='cage_update'),
    path('cage/<int:pk>/delete/', views.CageDeleteView.as_view(), name='cage_delete'),
    path('allergy/', views.allergylistview, name='allergy_list'),
    path('allergy/create/', views.allergycreateview, name='allergy_create'),
    path('allergy/<int:pk>/delete/', views.AllergyDeleteView.as_view(), name='allergy_delete'),
    path('medication/', views.medicationlistview, name='medication_list'),
    path('medication/create/', views.medicationcreateview, name='medication_create'),
    path('medication/<int:pk>/delete/', views.MedicationDeleteView.as_view(), name='medication_delete'),
    # Data exports
    path('export-all-xls/', views.all_animal_export, name='all_xls_export'),
    path('export-all-xls/', views.all_available_export, name='available_xls_export'),
    path('export-all-xls/', views.all_quarantine_export, name='quarantine_xls_export'),
    path('export-all-xls/', views.all_adopted_export, name='adopted_xls_export'),
    path('export-all-xls/', views.all_reserved_export, name='reserved_xls_export'),
]