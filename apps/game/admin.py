from django.contrib import admin
from apps.game import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Game)
