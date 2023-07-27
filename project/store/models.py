from django.db import models

# Create your models here.

class About(models.Model):
    text = models.TextField(verbose_name="Izoh")
    photo = models.ImageField(upload_to='about/', verbose_name="Rasmi")
    address = models.CharField(max_length=255, verbose_name="Manzil")
    phone = models.CharField(max_length=18, verbose_name="Telefon nomer")
    email = models.EmailField(verbose_name="Email")


class GalleryText(models.Model):
    text = models.TextField(verbose_name="Izoh")


class Gallery(models.Model):
    text = models.ForeignKey(GalleryText, on_delete=models.CASCADE, verbose_name="Matni")
    image = models.ImageField(upload_to='gallery/', verbose_name="Rasm")


class Service(models.Model):
    logo = models.ImageField(upload_to='logo/', verbose_name="Logosi")
    title = models.CharField(max_length=50, verbose_name="Nomi")
    content = models.TextField(verbose_name="Matni")


class Comment(models.Model):
    author = models.CharField(max_length=50, verbose_name="Author ismi")
    text = models.TextField(verbose_name="Commet matni")


class Message(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ismi")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=18, verbose_name="Telefon nomeri")
    message = models.TextField(verbose_name="Xabar")
