from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Article
    fields = '_all__'