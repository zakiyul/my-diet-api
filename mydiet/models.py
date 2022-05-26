from django.db import models

class CaraPakai(models.Model):
  slug = models.CharField(max_length=100)
  richText = models.TextField()

  def __str__(self):
    return self.slug

class Ingredients(models.Model):
  slug = models.CharField(max_length=100)
  richText = models.TextField()

  def __str__(self):
    return self.slug

class ObatDiet(models.Model):
  nama = models.CharField(max_length=255)
  harga = models.IntegerField()
  caraPakai = models.OneToOneField(CaraPakai, on_delete=models.CASCADE)
  ingredients = models.OneToOneField(Ingredients, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='obat_diet/', null=True)

  def __str__(self):
    return self.nama
