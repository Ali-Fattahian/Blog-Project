# Generated by Django 3.2.5 on 2021-10-15 15:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20211015_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]