from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.Quote)
admin.site.register(models.Review)