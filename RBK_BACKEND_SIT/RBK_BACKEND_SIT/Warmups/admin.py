from django.contrib import admin

# Register your models here.


# Register your models here.
from .models import Warmups, WarmupsAdmin

admin.site.register(Warmups, WarmupsAdmin)
