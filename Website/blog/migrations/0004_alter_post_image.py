# Generated by Django 3.2.6 on 2021-10-31 11:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='posts/default_post_image.jpg', max_length=255, null=True, verbose_name='image'),
        ),
    ]
