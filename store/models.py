from django.db import models

# Create your models here.
class Store(models.Model):  # 가게 정보
    name = models.CharField(max_length=200)  # 가게 이름
    location = models.CharField(max_length=400)  # 위치
    phone = models.CharField(max_length=30, blank=True, null=True)  # 전화번호
    is_cafe = models.BooleanField(default=True)  # True -> 카페, False -> 레스토랑
    image = models.ImageField(upload_to='dp/store_images/%Y/%m/%d', blank=True, null=True)  # 가게 이미지
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # 할인 정보

    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)