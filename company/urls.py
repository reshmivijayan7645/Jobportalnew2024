from django.urls import path
from . import views

urlpatterns = [
    path("list", views.list_company),
    # path("login", views.company_login_view, name='login'),
    path("login/", views.login_view, name='company_login'),
    path("job", views.company_job_view, name='job'),
    path('add_job', views.add_job, name='add_job'),
    path('remove_job/<int:job_id>/', views.remove_job, name='remove_job'),
    path('view_application', views.view_application, name='view_application'),
    
]


