from django.urls import  path
from rest_framework_simplejwt.views import (
  TokenRefreshView,
)
from . import views

urlpatterns = [
  path('products/', views.product_list),
  path('products/<int:id>', views.detail_product),
  path('articles/', views.article_list),
  path('articles/<int:id>', views.detail_article),

  path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]