from django.contrib import admin
from myapp import models


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Person, admin.ModelAdmin)
admin.site.register(models.Profession, admin.ModelAdmin)
