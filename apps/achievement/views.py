from django.shortcuts import render, redirect
from .models import Achievement
from apps.targets.models import Categories,Target
from django.views import View
from .forms import Edit_Achievement_Form

from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import AchievementSerializer,TargetSerializer
from datetime import  datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from  apps.setting.helper import set



class ListAchievement(View):

    template_name = 'list_achievement.html'
    def get(self,request):
        achievement_list = Achievement.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(achievement_list,15)
        try:
            achievements = paginator.page(page)
        except PageNotAnInteger:
            achievements = paginator.page(1)
        except EmptyPage:
            achievements = paginator.page(paginator.num_pages)


        return render(request,self.template_name,{
            'achievement':achievements
        })

class AddReport(View):
    template_name = ''
    def get(self,request):
        pass

class EditReport(View):
    template_name = 'edit_achievement.html'
    def get(self,request,id):
        obj = Achievement.objects.get(id=id)
        data = {
            'id':id,
            'target': obj.target,
            'categories':obj.category,
            'activity':obj.activity,
            'target_set':obj.target_set,
            'unit':obj.unit,
            'real':obj.actual,
            'date': obj.date
        }

        form = Edit_Achievement_Form(initial=data)
        print(form)
        return render(request, self.template_name,{
            'form':form,
            'id':id
        })

class Update_Achievement(View):
    def post(self,request,id):
        form = Edit_Achievement_Form(request.POST)
        if form.is_valid():
            obj = Achievement.objects.get(id=id)
            obj.target = form.cleaned_data['target']
            obj.category = form.cleaned_data['categories']
            obj.activity = form.cleaned_data['activity']
            obj.target_set = form.cleaned_data['target_set']
            obj.unit = form.cleaned_data['unit']
            obj.actual = form.cleaned_data['real']
            obj.date = datetime.strptime(form.cleaned_data['date'],"%Y-%m-%d").date()
            obj.save()
            return redirect('/targets/achievement/list')
        else:
            print("Gak Valid Iki")
            return HttpResponse(form.errors)


class Delete_Achievement(View):
    def get(self,request,id):
        obj = Achievement.objects.get(id=id)
        obj.delete()
        return redirect('/targets/achievement/list')


class AchievementApi(View):
    @csrf_exempt
    def get(self,request):
        achievement = Achievement.objects.all()
        serializer = AchievementSerializer(achievement,many=True)
        return JsonResponse(serializer.data,safe=False)

class TargetApi(View):
    @csrf_exempt
    def get(self,request):
        target = Target.objects.all()
        ser = TargetSerializer(target,many=True)
        return JsonResponse(ser.data,safe = False)
