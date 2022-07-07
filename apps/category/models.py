from django.db import models

class Category(models.Model):
    record_id = models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=200)

class Sub_category(models.Model):
    record_id = models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=200)