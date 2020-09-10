from django.db import models


# Create your models here.
class BlmWheel(models.Model):
    img = models.CharField(max_length=64)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'blm_wheel'
