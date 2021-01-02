from django.contrib import admin
from .models import Categories,Target

admin.site.register(Categories)


class TargetAdmin(admin.ModelAdmin):
    list_display = ("categories","activity","target_set","unit")




admin.site.register(Target,TargetAdmin)
