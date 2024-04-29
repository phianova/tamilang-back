from django.contrib import admin

# Register your models here.
from .models import Letter, UserLearning

admin.site.register(Letter)
admin.site.register(UserLearning)