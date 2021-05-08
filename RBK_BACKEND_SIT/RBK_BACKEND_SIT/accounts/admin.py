from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name', 'first_name','email')
    list_display =('email','id','user_name','is_active', 'first_name','is_staff','Last_name')
    ordering = ('-id',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name','Last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser')}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name','Last_name' ,'password1', 'password2', 'is_active', 'is_staff','is_superuser')}
         ),
    )
 
  


admin.site.register(NewUser,UserAdminConfig )