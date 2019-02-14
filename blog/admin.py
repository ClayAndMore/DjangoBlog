from django.contrib import admin

# Register your models here.

from django.contrib import admin
from blog import models

admin.site.register(models.Essay)
admin.site.register(models.Images)
admin.site.register(models.Message)
