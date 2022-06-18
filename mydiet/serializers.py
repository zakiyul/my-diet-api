from rest_framework import serializers
from . import models

class CaraPakaiSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.CaraPakai
    fields = '__all__'

class IngredientsSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Ingredients
    fields = '__all__'

class ObatDietSerializerGET(serializers.ModelSerializer):
  caraPakai = CaraPakaiSerializer(read_only=True)
  ingredients = IngredientsSerializer(read_only=True)

  class Meta:
    model = models.ObatDiet
    fields = ('id','nama','harga','image','caraPakai','ingredients')

class ObatDietSerializerPOST(serializers.ModelSerializer):
  class Meta:
    model = models.ObatDiet
    fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Article
    fields = '_all__'