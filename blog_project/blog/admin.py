from django.contrib import admin
import models


# Register your models here.
admin.site.register(models.BlogUser)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Article)
