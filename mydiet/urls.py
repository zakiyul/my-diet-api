from django.urls import  path
from . import views

urlpatterns = [
  path('items/', views.obatDiet_list),
  path('items/<int:id>', views.detail_obatDiet),
  path('articles/', views.article_list),
  path('articles/<int:id>', views.detail_article)
]