import email
from locale import currency
from turtle import title
from django.db import models
from pkg_resources import require

class DataHub(models.Model):
    email = models.EmailField(verbose_name="Почта")
    hub_link = models.CharField(max_length=300)
    phone = models.CharField(max_length=20,unique=True,default='0')
    def __str__(self):
        return "Hub " + self.phone

class Category(models.Model):
    hub = models.ForeignKey(DataHub, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class ProductItem(models.Model):
    hub = models.ForeignKey(DataHub, on_delete=models.PROTECT)
    p_id = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    image_link = models.CharField(max_length=300)
    link = models.CharField(max_length=300)
    currency_code = models.CharField(max_length=10)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
