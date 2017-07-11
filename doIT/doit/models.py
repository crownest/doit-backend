from django.db import models

class User(models.Model):
    e_mail=models.EmailField(max_length=200, blank=True, verbose_name="E-Posta")
    first_name=models.CharField(max_length=200, blank=True, verbose_name="Ad")
    last_name=models.CharField(max_length=200, blank=True, verbose_name="Soyad")
    password=models.CharField(max_length=50, blank=True, verbose_name="Şifre")

class Tasks(models.Model):
    title=models.CharField(max_length=1000, blank=True, verbose_name="Hatırlatma")
    user=models.ForeignKey(User, verbose_name="Kullanıcı")
