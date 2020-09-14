from django.db import models


# Create your models here.
class User(models.Model):
    # 昵称，要唯一
    userName = models.CharField(max_length=20, unique=True)
    # 密码
    userPasswd = models.CharField(max_length=20)
    # 手机号
    userPhone = models.CharField(max_length=20, unique=True)
    # 地址
    userAdderss = models.CharField(max_length=100, null=True, blank=True)
    # 头像路径
    userImg = models.ImageField(upload_to='%Y/%m/%d/img', null=True, blank=True)
    # 等级
    userRank = models.CharField(max_length=16)
    # touken验证值，每次登陆之后都会更新
    userToken = models.CharField(max_length=50)

    class Meta:
        db_table = 'user'
