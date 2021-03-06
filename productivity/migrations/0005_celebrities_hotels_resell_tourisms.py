# Generated by Django 3.2.9 on 2021-11-19 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productivity', '0004_auto_20211119_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tourisms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, default='India', max_length=300, null=True)),
                ('state', models.CharField(blank=True, default='Meghalaya', max_length=300, null=True)),
                ('address', models.CharField(blank=True, default='Jowai', max_length=300, null=True)),
                ('contact', models.CharField(blank=True, default='contact', max_length=300, null=True)),
                ('image', models.CharField(blank=True, default='image', max_length=300)),
                ('title', models.TextField(blank=True, default='title', null=True)),
                ('content', models.TextField(blank=True, default='content', null=True)),
                ('isApproved', models.BooleanField(default=False, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default='Tourism', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, default='India', max_length=300, null=True)),
                ('state', models.CharField(blank=True, default='Meghalaya', max_length=300, null=True)),
                ('address', models.CharField(blank=True, default='Jowai', max_length=300, null=True)),
                ('contact', models.CharField(blank=True, default='contact', max_length=300, null=True)),
                ('image', models.CharField(blank=True, default='image', max_length=300)),
                ('title', models.TextField(blank=True, default='title', null=True)),
                ('content', models.TextField(blank=True, default='content', null=True)),
                ('isApproved', models.BooleanField(default=False, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default='Category', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, default='India', max_length=300, null=True)),
                ('state', models.CharField(blank=True, default='Meghalaya', max_length=300, null=True)),
                ('address', models.CharField(blank=True, default='Jowai', max_length=300, null=True)),
                ('contact', models.CharField(blank=True, default='contact', max_length=300, null=True)),
                ('image', models.CharField(blank=True, default='image', max_length=300)),
                ('title', models.TextField(blank=True, default='title', null=True)),
                ('content', models.TextField(blank=True, default='content', null=True)),
                ('isApproved', models.BooleanField(default=False, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default='Hotels', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Celebrities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, default='India', max_length=300, null=True)),
                ('state', models.CharField(blank=True, default='Meghalaya', max_length=300, null=True)),
                ('address', models.CharField(blank=True, default='Jowai', max_length=300, null=True)),
                ('contact', models.CharField(blank=True, default='contact', max_length=300, null=True)),
                ('image', models.CharField(blank=True, default='image', max_length=300)),
                ('title', models.TextField(blank=True, default='title', null=True)),
                ('content', models.TextField(blank=True, default='content', null=True)),
                ('isApproved', models.BooleanField(default=False, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default='Category', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
