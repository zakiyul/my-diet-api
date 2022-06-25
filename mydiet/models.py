from django.db import models

class Product(models.Model):
    nama            = models.CharField(max_length=255)
    harga           = models.IntegerField()
    rating          = models.FloatField()
    deskripsi       = models.TextField()
    caraPakai       = models.TextField()
    ingredients     = models.TextField()
    image           = models.ImageField(upload_to='products/', null=True)

    def __str__(self):
        return self.nama

class Article(models.Model):
  title = models.CharField(max_length=255)
  image = models.ImageField(upload_to='article/', null=True)
  link  = models.CharField(max_length=255)

  def __str__(self):
    return self.title
