# Generated by Django 3.2.9 on 2021-11-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0003_auto_20211119_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.CharField(blank=True, default='image', max_length=300),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='image',
            field=models.CharField(blank=True, default='image', max_length=300),
        ),
        migrations.AlterField(
            model_name='ownbusiness',
            name='image',
            field=models.CharField(blank=True, default='image', max_length=300),
        ),
        migrations.AlterField(
            model_name='shops',
            name='image',
            field=models.CharField(blank=True, default='image', max_length=300),
        ),
    ]
