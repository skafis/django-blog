from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DataField(db_index=True, auto_now_add=True)
    category = models.Foreignkey('blog.category')
    
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug= models.SlugField(max_length=100, db_index=True)