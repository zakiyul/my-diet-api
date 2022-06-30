from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from . import models

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
     token = super().get_token(user)
     token['username'] = user.username
     return token

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Article
    fields = '__all__'