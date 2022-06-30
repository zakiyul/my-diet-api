from functools import partial
from django.http import HttpResponse, response
from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView

from . import models
from . import serializers

class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = serializers.MyTokenObtainPairSerializer

@api_view(['GET','POST'])
def product_list(req):
    if req.method == 'GET':
        product = models.Product.objects.all()
        serializer = serializers.ProductSerializer(product, many=True)
        return Response(serializer.data)

    elif req.method == 'POST':
        serializer = serializers.ProductSerializer(data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def detail_product(req, id):
    try:
        product = models.Product.objects.get(pk=id)
    except models.Product.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = serializers.ProductSerializer(product)
        return Response(serializer.data)

    elif req.method == 'PATCH':
        serializer = serializers.ProductSerializer(product, data=req.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif  req.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def article_list(request):
  if request.method == 'GET':
    articles = models.Article.objects.all()
    serializer = serializers.ArticleSerializer(articles, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = serializers.ArticleSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH','DELETE'])
def detail_article(request, id):
  try:
    article = models.Article.objects.get(pk=id)
  except models.ObatDiet.DoesNotExist:
    return HttpResponse(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = serializers.ArticleSerializer(article)
    return Response(serializer.data)
  
  elif request.method == 'PATCH':
    serializer = serializers.ArticleSerializer(article, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)