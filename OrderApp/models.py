from django.db import models

from MarketApp.models import BlmGoods
from UserApp.models import User


class BlmOrder(models.Model):
    o_user = models.ForeignKey(User)
    o_time = models.DateTimeField(auto_now_add=True)
    o_total_price = models.FloatField()

    class Meta:
        db_table = 'blm_order'


class Blm_OrderGoods(models.Model):
    og_order = models.ForeignKey(BlmOrder)
    # 购物车里选择购买的商品
    og_good = models.ForeignKey(BlmGoods)

    og_c_good_num = models.IntegerField()

    class Meta:
        db_table = 'blm_ordergoods'
