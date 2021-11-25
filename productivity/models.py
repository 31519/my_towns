from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=300, null=True, blank=True, default="Category")
    country = models.CharField(max_length=300, blank=True, null=True, default='India')
    state = models.CharField(max_length=300, blank=True, null=True, default='Meghalaya')
    address = models.CharField(max_length=300, blank=True, null=True, default='Jowai')
    contact = models.CharField(max_length=300, blank=True, null=True, default='contact')
    image = models.CharField(max_length=300, blank=True, default='image')
    title = models.TextField(blank=True, null=True, default='title')
    content = models.TextField(blank=True, null=True, default='content')
    isApproved = models.BooleanField(default=False, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)


class Advertisement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=300, null=True, blank=True, default="Category")
    country = models.CharField(max_length=300, blank=True, null=True, default='India')
    state = models.CharField(max_length=300, blank=True, null=True, default='Meghalaya')
    address = models.CharField(max_length=300, blank=True, null=True, default='Jowai')
    contact = models.CharField(max_length=300, blank=True, null=True, default='contact')
    image = models.CharField(max_length=300, blank=True, default='image')
    title = models.TextField(blank=True, null=True, default='title')
    content = models.TextField(blank=True, null=True, default='content')
    isApproved = models.BooleanField(default=False, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)


class OwnBusiness(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=300, null=True, blank=True, default="Category")
    country = models.CharField(max_length=300, blank=True, null=True, default='India')
    state = models.CharField(max_length=300, blank=True, null=True, default='Meghalaya')
    address = models.CharField(max_length=300, blank=True, null=True, default='Jowai')
    contact = models.CharField(max_length=300, blank=True, null=True, default='contact')
    image = models.CharField(max_length=300, blank=True, default='image')
    title = models.TextField(blank=True, null=True, default='title')
    content = models.TextField(blank=True, null=True, default='content')
    isApproved = models.BooleanField(default=False, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)

class Shops(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    category = models.CharField(max_length=300, null=True, blank=True, default="Category")
    country = models.CharField(max_length=300, blank=True, null=True, default='India')
    state = models.CharField(max_length=300, blank=True, null=True, default='Meghalaya')
    address = models.CharField(max_length=300, blank=True, null=True, default='Jowai')
    contact = models.CharField(max_length=300, blank=True, null=True, default='contact')
    image = models.CharField(max_length=300, blank=True, default='image')
    title = models.TextField(blank=True, null=True, default='title')
    content = models.TextField(blank=True, null=True, default='content')
    isApproved = models.BooleanField(default=False, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)

class Celebrities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=300, null=True, blank=True, default="Category")
    country = models.CharField(max_length=300, blank=True, null=True, default='India')
    state = models.CharField(max_length=300, blank=True, null=True, default='Meghalaya')
    address = models.CharField(max_length=300, blank=True, null=True, default='Jowai')
    contact = models.CharField(max_length=300, blank=True, null=True, default='contact')
    image = models.CharField(max_length=300, blank=True, default='image')
    title = models.TextField(blank=True, null=True, default='title')
    content = models.TextField(blank=True, null=True, default='content')
    isApproved = models.BooleanField(default=False, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)


class Hotels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    category = models.CharField(max_length=300, null=True, blank=True, default="Category")
    country = models.CharField(max_length=300, blank=True, null=True, default='India')
    state = models.CharField(max_length=300, blank=True, null=True, default='Meghalaya')
    address = models.CharField(max_length=300, blank=True, null=True, default='Jowai')
    contact = models.CharField(max_length=300, blank=True, null=True, default='contact')
    image = models.CharField(max_length=300, blank=True, default='image')
    title = models.TextField(blank=True, null=True, default='title')
    content = models.TextField(blank=True, null=True, default='content')
    isApproved = models.BooleanField(default=False, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)



class Tourisms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    category = models.CharField(max_length=300, null=True, blank=True, default="Category")
    country = models.CharField(max_length=300, blank=True, null=True, default='India')
    state = models.CharField(max_length=300, blank=True, null=True, default='Meghalaya')
    address = models.CharField(max_length=300, blank=True, null=True, default='Jowai')
    contact = models.CharField(max_length=300, blank=True, null=True, default='contact')
    image = models.CharField(max_length=300, blank=True, default='image')
    title = models.TextField(blank=True, null=True, default='title')
    content = models.TextField(blank=True, null=True, default='content')
    isApproved = models.BooleanField(default=False, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)


class Resell(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=300, null=True, blank=True, default="Category")
    country = models.CharField(max_length=300, blank=True, null=True, default='India')
    state = models.CharField(max_length=300, blank=True, null=True, default='Meghalaya')
    address = models.CharField(max_length=300, blank=True, null=True, default='Jowai')
    contact = models.CharField(max_length=300, blank=True, null=True, default='contact')
    image = models.CharField(max_length=300, blank=True, default='image')
    title = models.TextField(blank=True, null=True, default='title')
    content = models.TextField(blank=True, null=True, default='content')
    isApproved = models.BooleanField(default=False, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)