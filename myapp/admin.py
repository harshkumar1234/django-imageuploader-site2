from django.contrib import admin
from .models import Image
@admin.register(Image)
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list=('id','photo','date')
