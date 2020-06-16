from django.db import models
#Django Object Relational Mapper
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
