from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from django.contrib import messages
from django.views import View
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

class RegistrationView(View):
 def get(self,request):
    form=RegistrationForm()
    context={
   'form':form,
   
    }
    return render(request, 'signup.html',context)
 def post(self,request):
  form=RegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request,'Registration successfull')
   form.save()
   return redirect('admin-home')
  context={
   'form':form
  }
  return render(request, 'signup.html',context)
 
@login_required(login_url="login")
def admin_home(request):
    home=admin_task.objects.all()
    

    context={
        'home':home,
       
    }
    return render (request,'admin_home.html',context)

@login_required(login_url="login")
def admin_task_update(request,id):
    admin_task_update=admin_task.objects.get(id=id)
    form=admin_task_form(instance=admin_task_update)
    if request.method == 'POST':
        form=admin_task_form(request.POST,request.FILES,instance=admin_task_update)
        if form.is_valid():
            form.save()
            messages.success(request,"App updated successfully")
            return redirect('admin-home')
        else:
            form=admin_task_form(request.POST,instance=admin_task_update)
    context={
        'admin_task_update':admin_task_update,
        'form':form
    }
    return render(request,'update.html',context)
@login_required(login_url="login")
def admin_task_delete(request,id):
    admin_task_delete=admin_task.objects.get(id=id)
    name=admin_task.objects.all()
    if request.method == 'POST':
        messages.warning(request,"App deleted successfully")
        admin_task_delete.delete()
        return redirect('admin-home')
    context={
        'admin_task_delete':admin_task_delete
    }
    return render(request,'delete.html',context)
@login_required(login_url="login")
def admin_task_area(request):
    form=admin_task_form()
    if request.method == 'POST':
        form=admin_task_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'App added successfully')
            return redirect('admin-task-area')
    else:
        form=admin_task_form()        
    context={
        'form':form
    }
    return render(request,'admin_task_area.html',context)
def user(request):
   pass
   return render(request,'profile.html')
def point(request):
   pass
   return render(request,'points.html')
@login_required(login_url="login")
def user_total_points(request):
    user = request.user
    user_points = UserPoint.objects.filter(user=user)
    total_points = sum(point.points_earned for point in user_points)

    return render(request, 'points.html', {'total_points': total_points})

@login_required(login_url="login")
def upload_screenshot(request, id):
    app = admin_task.objects.get(pk=id)
    user = request.user
    user_point, created = UserPoint.objects.get_or_create(user=user, app=app)
    if request.method == 'POST':
        screenshot = request.FILES.get('screenshot')
        if screenshot:
            user_point.points_earned +=  app.points
            user_point.save()
            messages.success(request,"Screenshot uploaded successfully!")
    return render (request,"task.html")

@login_required(login_url="login")
def completed_task(request):
   completed_task=UserPoint.objects.filter(user=request.user)
   return render(request,"completed_task.html",{'completed_task':completed_task})