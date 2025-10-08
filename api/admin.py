from django.contrib import admin
from .models import BasicText

# Register your models here.

class BasicTextAdmin(admin.ModelAdmin):
    pass

admin.site.register(BasicText, BasicTextAdmin)


