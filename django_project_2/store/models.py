from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, null=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default='no_photo.jpg', upload_to='products_photo/',)
    category = models.ManyToManyField(Category, related_name="products")


    def __str__(self):
        return self.name
