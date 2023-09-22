from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    titulo         = models.CharField(max_length=255)
    subtitulo      = models.CharField(max_length=255)
    contenido      = RichTextField(null=True)
    autor          = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(default=timezone.now)
    imagen         = models.ImageField(upload_to='images')
    
