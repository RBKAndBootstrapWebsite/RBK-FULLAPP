from django.contrib import admin
from .models import NewUser
# from django.contrib.auth.admin import UserAdmin
# from django.forms import TextInput, Textarea, CharField
# from django import forms
# from django.db import models

# class UserAsminConfig(UserAdmin):
#     model = NewUser
#     list_display =('email','id','user_name','is_active', 'first_name','is_staff','Last_name')
#     ordering = ('-id',)
  
 
  


admin.site.register(NewUser )