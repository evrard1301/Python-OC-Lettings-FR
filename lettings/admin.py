from django.contrib import admin

from lettings import models

admin.site.register(models.Address)
admin.site.register(models.Letting)
