from django.contrib import admin
from .models import CustomUser

# Register custom user model


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
