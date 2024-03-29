# Generated by Django 3.2.6 on 2021-10-31 11:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, default='users_profile_picture/default_user_image.png', max_length=255, null=True, verbose_name='image'),
        ),
    ]
