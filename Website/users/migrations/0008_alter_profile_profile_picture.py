# Generated by Django 3.2.6 on 2021-10-30 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='../static/default_user_image.png', upload_to='users_profile_picture'),
        ),
    ]