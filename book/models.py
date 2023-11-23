from django.db import models
from django.urls import reverse

# 모델 만들고 반드시 migration 하기!
# python manage.py makemigrations book
# python manage.py migrate book

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)

    def __str__(self):
        return self.title #문자열로 return
    
    def get_absolute_url(self):
        return reverse("book:list")
    
