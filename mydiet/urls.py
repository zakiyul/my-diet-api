from django.urls import  path
from . import views

urlpatterns = [
  path('products/', views.product_list),
  path('products/<int:id>', views.detail_product),
  path('articles/', views.article_list),
  path('articles/<int:id>', views.detail_article)
]