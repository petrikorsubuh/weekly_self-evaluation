from django.shortcuts import render,redirect
from .models import Categories,Target
from .forms import FormCategories,Formtarget
from django.views import View
from django.http import HttpResponse

class CategoriesList(View):
    template_name = 'list_category.html'
    def get (self,request):
        categories = Categories.objects.all()
        return render(request,self.template_name,{
            'cat':categories,
        })

class AddCategories(View):
    template_name ='add_categories.html'
    def get(self,request):
        form = FormCategories(request.POST)
        return render(request,self.template_name,{
            'form':form,
        })

class SaveCategories(View):
    def post(self,request):
        form = FormCategories(request.POST)
        category = Categories()
        if form.is_valid():
            category.name = form.cleaned_data['name']
            category.save()
            return redirect('/targets')

class UpdateCategories(View):
    template_name = 'edit_categories.html'
    def get(self,request,id):
        categories = Categories.objects.get(id=id)
        data = {
            'name':categories.name,
            'id':categories.id
        }
        form = FormCategories(initial=data)
        return render(request,self.template_name,{
            'form':form,
            'id':id
        })

    def post(self,request,id):
        form = FormCategories(request.POST)
        if form.is_valid():
            categories = Categories.objects.get(id=form.cleaned_data['id'])
            print(categories)
            categories.name = form.cleaned_data['name']
            categories.save()

            return redirect('/targets')


class DeleteCategories(View):
    def get(self,request,id):
        cat = Categories.objects.get(id=id)
        cat.delete()
        return redirect('/categories')


class Lits_Activity(View):
    template_name ='list_activity.html'
    def get(self,request,id):
        cat_tittle = Categories.objects.get(id=id)
        activity = Target.objects.filter(categories=id)
        return render(request,self.template_name,{
            'activity':activity,
            'tittle':cat_tittle.name,
            'id':id
        })

class AddActivity(View):
    template_name='add_activity.html'
    def get(self,request,id):
        form = Formtarget(request.POST)
        tittle = Categories.objects.get(id=id)
        print(tittle)
        return render(request,self.template_name,{
            'form':form,
            'id':id,
            "tittle":tittle
        })

class SaveActivity(View):
    def post(self,request,id):
        form = Formtarget(request.POST)
        activity = Target()
        print(request.POST)

        if form.is_valid():
            activity.categories = Categories.objects.get(id=id)
            activity.activity = form.cleaned_data['activity']
            activity.target_set = form.cleaned_data['target_set']
            activity.unit = form.cleaned_data['unit']
            activity.save()
            return redirect(f'/targets/{id}/activity')
        else:
            return HttpResponse(request,form.errors)

class EditActivity(View):
    template_name = 'edit_activity.html'
    def get(self,request,id,activity_id):
        target =Target.objects.get(id=activity_id)
        data = {
            'activity': target.activity,
            'target_set':target.target_set,
            'unit':target.unit
        }
        form = Formtarget(initial=data)
        return render(request,self.template_name,{
            'form':form,
            'id':id,
            'activity_id':activity_id,
        })

    def post(self,request,id,activity_id):
        target = Target.objects.get(id=activity_id)
        form = Formtarget(request.POST)
        if form.is_valid():
            target.activity = form.cleaned_data['activity']
            target.target_set = form.cleaned_data['target_set']
            target.unit = form.cleaned_data['unit']
            target.save()
            return redirect(f'/targets/{id}/activity')
        return HttpResponse(request,form.errors)

class DeleteActivity(View):
    def get(self,requets,id,activity_id):
        activity = Target.objects.get(id=activity_id)
        activity.delete()
        return redirect(f'/targets/{id}/activity')
