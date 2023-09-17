from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=128, null=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    category_choices = [
        ("레저/체육/공원", "레저/체육/공원"),
        ("문화관광/명소", "문화관광/명소"),
        ("전시/공연", "전시/공연"),
    ]  # 게시글 등록할 때 고전미술인지, 현대미술인지 체크하는 코드
    category = models.CharField(max_length=50, choices=category_choices, null=True)  
    parking_choices = [
        ("무료주차", "무료주차"),
        ("유료주차", "유료주차"),
    ]  
    parking = models.CharField(max_length=50, choices=parking_choices, null=True)
    dis_parking_choices = [
        ("장애인 주차구역 있음", "장애인 주차구역 있음"),
        ("장애인 주차구역 없음", "장애인 주차구역 없음"),
    ]  
    dis_parking = models.CharField(max_length=50, choices=dis_parking_choices, null=True)
    big_parking_choices = [
        ("대형차 주차 불가", "대형차 주차 불가"),
        ("대형차 주차 가능", "대형차 주차 가능"),
    ]  
    big_parking = models.CharField(max_length=50, choices=big_parking_choices, null=True)
    wheelchair_choices = [
        ("휠체어 대여 불가", "휠체어 대여 불가"),
        ("휠체어 대여 가능", "휠체어 대여 가능"),
    ]  
    wheelchair = models.CharField(max_length=50, choices=wheelchair_choices, null=True)
    toilet_choices = [
        ("장애인 화장실 없음", "장애인 화장실 없음"),
        ("장애인 화장실 있음", "장애인 화장실 있음"),
    ]  
    toilet = models.CharField(max_length=50, choices=toilet_choices, null=True)
    braille_choices = [
        ("장애인 안내 점자 없음", "장애인 안내 점자 없음"),
        ("장애인 안내 점자 있음", "장애인 안내 점자 있음"),
    ]  
    braille = models.CharField(max_length=50, choices=braille_choices, null=True)
    audio_choices = [
        ("오디오 가이드 없음(한국어)", "오디오 가이드 없음(한국어)"),
        ("오디오 가이드 있음(한국어)", "오디오 가이드 있음(한국어)"),
    ]  
    audio = models.CharField(max_length=50, choices=audio_choices, null=True)

class My(models.Model):
    author = models.ForeignKey(
        "account.User", null=True, on_delete=models.CASCADE
    )
    latitude = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=10, null=True)