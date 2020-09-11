from django.db import models


# 主页面的图片 模型
class HomeImg(models.Model):
    img = models.CharField(max_length=64)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True


# 图片循环播放 模型
class BlmWheel(HomeImg):
    class Meta:
        db_table = 'blm_wheel'


# 选择功能图片 模型
class BlmChoice(HomeImg):
    class Meta:
        db_table = 'blm_choice'


# 优惠券 模型
class BlmDiscount(HomeImg):
    class Meta:
        db_table = 'blm_discount'


# 品牌店 模型
class BlmBrand(HomeImg):
    class Meta:
        db_table = 'blm_brand'


# 限时活动 模型
class BlmActivity(HomeImg):
    img2 = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'blm_activity'


# 专属推荐 模型
class BlmRecommend(HomeImg):
    status = models.CharField(max_length=16, null=True, blank=True)
    now_price = models.IntegerField()
    ex_price = models.IntegerField()

    class Meta:
        db_table = 'blm_recommend'
