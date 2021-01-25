from django.shortcuts import render,redirect
from django.views import View
from .models import Profile
from django.contrib.auth.models import User
from .forms import RegisterForm,LoginForm
from django.http import HttpResponse
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from apps.achievement.tests import label_filter,date_filter
from apps.achievement.models import Achievement
from datetime import datetime
from apps.setting.forms import *
from apps.setting.models import Settings
from django.http import JsonResponse

class FromRegister(View):
    template_name = 'auth/register.html'
    def get(self,request):
        form = RegisterForm(request.POST)
        return render(request,self.template_name,{
            'form':form,
        })

class Register(View):
    def post(self,request):
        form = RegisterForm(request.POST,request.FILES)
        profile = Profile()
        user = User()
        if form.is_valid():
            obj = User.objects.filter(username = request.POST['username'])
            if obj:
                messages.error(request,'User sudah tersedia')
                return redirect('/register')
            else:
                if request.POST['password1'] == request.POST['password2']:
                    user.username = form.cleaned_data['username']
                    user.password1 = form.cleaned_data['password1']
                    user.set_password(user.password1)
                    user.first_name = form.cleaned_data['firstname']
                    user.last_name = form.cleaned_data['lastname']
                    user.save()
                    profile.user = user
                    profile.age = form.cleaned_data['gender']
                    try:
                        profile.photo = request.FILES['photo_profile']
                        profile.save()
                    except:
                        profile.save()
                    return redirect('/login')
                else:
                    messages.error(request,'password is not correct')
                    return redirect('/register')
        return redirect('/register')

class LoginView(View):
    template_name = 'auth/login.html'
    def get(self,request):
        form = LoginForm(request.POST)
        return render(request,self.template_name,{
            'form':form,
        })

class LoginProsses(View):
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            print('masuk pak eko')
            user_name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=user_name,password=password)
            if user is not None:
                login(request,user)
                return redirect('/targets/')
            else:
                return redirect('/login')
        else:
            messages.error(request,'Invalid username and password')
            return redirect('/login')


class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('/login')

class MemberLandingPage(View):
    template_name = 'member_landing_page.html'
    def get(self,request):
        # start_date = None
        # end_date = None
        form = SearchDateForm(request.POST)
        start_date_obj = Settings.objects.filter(set_property='start_date').values()[0]["value"]
        end_date_obj = Settings.objects.filter(set_property='end_date').values()[0]["value"]
        print(f"start_date landing page : {start_date_obj}")
        print(f"end_date landing page : {end_date_obj}")
        if len(start_date_obj)==10 and len(end_date_obj)==10:
            start_date = datetime.strptime(start_date_obj,"%Y-%m-%d")
            end_date = datetime.strptime(end_date_obj,"%Y-%m-%d")
        else:
            start_date,end_date = None,None
        # for sd in start_date_obj:
        #     if len(sd.value)==9:
        #         start_date = sd.value
        #     else:
        #         start_date=None
        #
        # for ed in end_date_obj:
        #     if len(ed.value)==9:
        #         end_date = ed.value
        #     else:
        #         end_date=None

        print(f"value of start_date {start_date}")
        print(f"value of end_date {end_date}")
        label = label_filter(start_date,end_date)
        data = date_filter(start_date,end_date)
        print(f"label : {label}")
        print(f"label : {data}")
        print(f"label count: {len(label)}")
        print(f"data count: {len(data)}")

        print(f"test form {request.POST}")
        print(f"test form {request.POST}")
        return render(request,self.template_name,{
            'kalimat':'udah masuk',
            'label':label,
            'data':data,
            'ln':len(data),
            'form':form

        })
    def post(self,request):
        form = SearchDateForm(request.POST)
        if form.is_valid():
            start_date_obj = Settings.objects.filter(set_property='start_date')
            print(f"kondisi awal start_date {start_date_obj.values()}")
            end_date_obj = Settings.objects.filter(set_property='end_date')
            print(f"kondisi awal end_date {end_date_obj.values()}")
            # start_date_obj[0]['value'] = form.cleaned_data["start_date"]
            # end_date_obj[0]['value'] = form.cleaned_data["end_date"]
            # start_date_obj.save()
            # end_date_obj.save()
            for sd in start_date_obj:
                sd.value = form.cleaned_data['start_date']
                sd.save()
            for ed in end_date_obj:
                ed.value = form.cleaned_data['end_date']
                ed.save()
            print(f"kondisi baru start_date {start_date_obj.values()}")
            print(f"kondisi baru end_date {end_date_obj.values()}")

            # start_date = datetime.strptime('2020-11-6',"%Y-%m-%d")
            # end_date = datetime.strptime('2021-1-22',"%Y-%m-%d")


            return redirect('/member_landingPage')
        else:
            HttpResponse(form.errors)


class SearchDate():
    template_name = 'member_landing_page.html'
    def post(self,request,start_date,end_date):
        print(f'parameter function start_date {start_date}')
        print(f'parameter function end_date {end_date}')
        form = SearchDateForm(request.POST)
        print(form.cleaned_data['start_date'])
        print(form.cleaned_data['end_date'])

        start_date = None
        end_date = None
        form = SearchDateForm(request.POST)
        # start_date = datetime.strptime('2020-11-6',"%Y-%m-%d")
        # end_date = datetime.strptime('2021-1-22',"%Y-%m-%d")
        label = label_filter(start_date,end_date)
        data = date_filter(start_date,end_date)
        print(f"test form {request.POST}")
        print(f"test form {request.POST}")
        return render(request,self.template_name,{
            'kalimat':'udah masuk',
            'label':label,
            'data':data,
            'ln':len(data),
            'form':form

        })


# class SearchRangeDate():
#         def post(self,request):
#             start_date = Settings.objects.filter(set_property = "start_date")
#             end_date = Settings.objects.filter(set_property = "end_date")
#             for sd in start_date:
#                 start_date_value = sd.value
#             for ed in end_date:
#                 end_date_value = ed.value
#             form = SearchDateForm(request.POST)
#             if form.is_valid():
#                 start_date_value = form.cleaned_data['start_date']
#                 end_date_value = form.cleaned_data['end_date']
