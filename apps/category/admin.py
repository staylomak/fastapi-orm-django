from django.contrib import admin

# Register your models here.
from apps.category.models import Category, Sub_category

admin.site.register(Category)
admin.site.register(Sub_category)