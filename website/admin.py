from django.contrib import admin

# Register your models here.
from .models import students
from .models import school


admin.site.register(students)
admin.site.register(school)