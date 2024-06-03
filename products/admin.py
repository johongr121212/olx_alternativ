from django.contrib import admin
from .models import Category,Product,Comment

# Register your models here. 
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','date','category','author']



admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)


