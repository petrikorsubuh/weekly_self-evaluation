from django.shortcuts import render
from .models import Achievement
from apps.targets.models import Categories,Target
from django.views import View

class ListAchievement(View):
    pass

class AddReport(View):
    template_name = ''
    def get(self,request):
        pass

class EditReport(View):
    pass
