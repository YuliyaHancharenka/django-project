from django.contrib import admin

# Register your models here.

from .models import Allcourses, Details

admin.site.register(Allcourses)
admin.site.register(Details)