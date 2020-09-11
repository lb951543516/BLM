from django.db import models


# Create your models here.

class BlmFoodType(models.Model):
    typeid = models.CharField(max_length=32)
    typename = models.CharField(max_length=64)
    childtypenames = models.CharField(max_length=128)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'blm_foodtype'


class BlmGoods(models.Model):
    productid = models.IntegerField()
    productimg = models.CharField(max_length=64)
    productname = models.CharField(max_length=64)
    productlongname = models.CharField(max_length=64)

    isxf = models.IntegerField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=32)
    price = models.FloatField()
    marketprice = models.FloatField()

    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=64)
    dealerid = models.IntegerField()
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'blm_goods'
