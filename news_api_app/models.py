from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Technology(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    category = models.CharField(max_length=200, null=True, blank=True, default='Technology')
    author = models.CharField(max_length=200, null=True, blank=True, default='Author')
    title = models.TextField(null=True, blank=True, default='Title')
    description = models.TextField(null=True, blank=True, default='Description')
    url= models.CharField(max_length=300, null=True, blank=True, default='Url')
    urlToImage= models.CharField(max_length=300, null=True, blank=True, default='UrlToImage')
    publishedAt = models.CharField(max_length=300, null=True,blank=True, default='PublishedAt')
    content = models.TextField(null=True, blank=True, default='content')
    # createdAt = models.DateTimeField(auto_now_add =True)
    createAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class Science(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    category = models.CharField(max_length=200, null=True, blank=True, default='Science')
    author = models.CharField(max_length=200, null=True, blank=True, default='Author')
    title = models.TextField(null=True, blank=True, default='Title')
    description = models.TextField(null=True, blank=True, default='Description')
    url= models.CharField(max_length=300, null=True, blank=True, default='Url')
    urlToImage= models.CharField(max_length=300, null=True, blank=True, default='UrlToImage')
    publishedAt = models.CharField(max_length=300, null=True,blank=True, default='PublishedAt')
    content = models.TextField(null=True, blank=True, default='content')
    # createdAt = models.DateTimeField(auto_now_add =True)
    createAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    category = models.CharField(max_length=200, null=True, blank=True, default='Business')
    author = models.CharField(max_length=200, null=True, blank=True, default='Author')
    title = models.TextField(null=True, blank=True, default='Title')
    description = models.TextField(null=True, blank=True, default='Description')
    url= models.CharField(max_length=300, null=True, blank=True, default='Url')
    urlToImage= models.CharField(max_length=300, null=True, blank=True, default='UrlToImage')
    publishedAt = models.CharField(max_length=300, null=True,blank=True, default='PublishedAt')
    content = models.TextField(null=True, blank=True, default='content')
    # createdAt = models.DateTimeField(auto_now_add =True)
    createAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class Health(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    category = models.CharField(max_length=200, null=True, blank=True, default='Health')
    author = models.CharField(max_length=200, null=True, blank=True, default='Author')
    title = models.TextField(null=True, blank=True, default='Title')
    description = models.TextField(null=True, blank=True, default='Description')
    url= models.CharField(max_length=300, null=True, blank=True, default='Url')
    urlToImage= models.CharField(max_length=300, null=True, blank=True, default='UrlToImage')
    publishedAt = models.CharField(max_length=300, null=True,blank=True, default='PublishedAt')
    content = models.TextField(null=True, blank=True, default='content')
    # createdAt = models.DateTimeField(auto_now_add =True)
    createAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)





class LocalNews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    category = models.CharField(max_length=200, null=True, blank=True, default='Lacal')
    author = models.CharField(max_length=200, null=True, blank=True, default='Author')
    title = models.TextField(null=True, blank=True, default='Title')
    description = models.TextField(null=True, blank=True, default='Description')
    url= models.CharField(max_length=300, null=True, blank=True, default='Url')
    urlToImage= models.CharField(max_length=300, null=True, blank=True, default='UrlToImage')
    publishedAt = models.CharField(max_length=300, null=True,blank=True, default='PublishedAt')
    content = models.TextField(null=True, blank=True, default='content')
    # createdAt = models.DateTimeField(auto_now_add =True)
    createAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)