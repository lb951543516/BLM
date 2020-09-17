from django.db import models

# Create your models here.
from MarketApp.models import BlmGoods
from UserApp.models import User


class BlmCar(models.Model):
    c_user = models.ForeignKey(User)
    c_good = models.ForeignKey(BlmGoods)
    g_num = models.IntegerField(default=1)
    is_buy = models.BooleanField(default=True)

    class Meta:
        db_table = 'blm_car'
