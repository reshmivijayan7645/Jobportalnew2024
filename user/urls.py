from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_login, name='user_login'),
    path("register", views.register_user, name='register'),
    path("logout", views.user_logout, name='logout'),
    path('profile', views.user_profile, name='user_profile'),
    path('jlist', views.job_list, name='jlist'),
    path('apply_job/<int:job_id>/', views.apply_job, name='apply_job'),


]
