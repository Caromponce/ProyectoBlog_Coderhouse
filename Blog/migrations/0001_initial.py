# Generated by Django 4.2.5 on 2023-09-21 18:10

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('subtitulo', models.CharField(max_length=255)),
                ('contenido', ckeditor.fields.RichTextField(null=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('imagen', models.ImageField(upload_to='images')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
