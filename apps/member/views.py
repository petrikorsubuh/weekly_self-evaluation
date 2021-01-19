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
        start_date = datetime.strptime('2020-11-6',"%Y-%m-%d")
        end_date = datetime.strptime('2021-1-22',"%Y-%m-%d")
        label = label_filter(start_date,end_date)
        data = date_filter(start_date,end_date)
        return render(request,self.template_name,{
            'kalimat':'udah masuk',
            'label':label,
            'data':data,
            'ln':len(data)
        })
