# studies/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.study_list, name='home'),
    path('add/', views.study_create, name='add_study'),
    path('edit/<int:pk>/', views.study_update, name='study_list'),
    path('delete/<int:pk>/', views.study_delete, name='delete_study'),
    path('view/<int:pk>/', views.study_view, name='view_study'),
]
