from django.db import models


# Create your models here.
class User(models.Model):
    # 用户名，要唯一
    userName = models.CharField(max_length=20, unique=True)
    # 昵称
    nickName = models.CharField(max_length=32, null=True, blank=True)
    # 密码
    userPasswd = models.CharField(max_length=256)
    # 手机号
    userPhone = models.CharField(max_length=20, unique=True)
    # 地址
    userAdderss = models.CharField(max_length=100, null=True, blank=True)
    # 头像路径
    userImg = models.ImageField(upload_to='%Y/%m/%d/img', null=True, blank=True)
    # 邮箱
    userEmail = models.CharField(max_length=64, unique=True)
    # 等级
    userRank = models.CharField(max_length=16, default='普通用户')
    # touken验证值，每次登陆之后都会更新
    userToken = models.CharField(max_length=256)
    # 是否邮箱激活帐号
    active = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'


class Address(models.Model):
    userId = models.IntegerField()
    consignee = models.CharField(max_length=16)
    userPhone = models.CharField(max_length=20)
    detailAdd = models.CharField(max_length=128)
    isselect = models.BooleanField(default=False)

    class Meta:
        db_table = 'address'
