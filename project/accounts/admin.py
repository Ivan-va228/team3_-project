from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('nickname', 'email', 'is_staff', 'is_active')  
    ordering = ('nickname',)  
    search_fields = ('nickname', 'email')  

admin.site.register(CustomUser, CustomUserAdmin)
