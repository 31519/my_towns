# Generated by Django 3.2.9 on 2021-11-13 06:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news_api_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='technology',
            name='createAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]