from django.contrib import admin
from .models import CustomUser

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser, UserAdmin)
