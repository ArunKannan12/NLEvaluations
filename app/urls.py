from . import views
from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm,redirect_authenticated_user=True) , name='login'),
    path("logout/", auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path("admin-home", views.admin_home, name="admin-home"),
    path("admin_task_area",views.admin_task_area,name="admin-task-area"),
    path("admin_task_update/<int:id>/",views.admin_task_update,name='admin_task_update'),
    path("admin_task_delete/<int:id>/",views.admin_task_delete,name='admin_task_delete'),

    path("user-profile",views.user,name="user-profile"),
    path("user-points", views.point, name="user-points"),
    path('user_total_points/', views.user_total_points, name='user_total_points'),
    path('apps/<int:id>/', views.upload_screenshot, name='upload_screenshot'),
    path('completed-task',views.completed_task,name="completed-task")
   
]
