from django.urls import  path
from . import views

urlpatterns = [
  path('items/', views.obatDiet_list),
  path('items/<int:id>', views.detail_obatDiet)
]