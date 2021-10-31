# Generated by Django 3.2.6 on 2021-10-31 11:29

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/df2vyrbdr/image/upload/v1635679583/default_user_image_lwehod.png', max_length=255, null=True, verbose_name='image'),
        ),
    ]