from functools import partial
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import models
from . import serializers

@api_view(['GET','POST'])
def obatDiet_list(request):
  if request.method == 'GET':
    obats = models.ObatDiet.objects.all()
    serializer = serializers.ObatDietSerializerGET(obats, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = serializers.ObatDietSerializerPOST(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH','DELETE'])
def detail_obatDiet(request, id):
  try:
    obat = models.ObatDiet.objects.get(pk=id)
  except models.ObatDiet.DoesNotExist:
    return HttpResponse(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = serializers.ObatDietSerializerGET(obat)
    return Response(serializer.data)
  
  elif request.method == 'PATCH':
    serializer = serializers.ObatDietSerializerGET(obat, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    obat.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)