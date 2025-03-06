from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default='no_photo.jpg', upload_to='products_photo/',)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

