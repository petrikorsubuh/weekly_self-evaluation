from django.contrib import admin
from .models import *

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('target','category','activity','target_set','actual','date')

admin.site.register(Achievement,AchievementAdmin)

