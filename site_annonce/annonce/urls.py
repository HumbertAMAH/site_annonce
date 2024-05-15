
from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('job_list/', views.job_list, name='job_list'),
    path('jobdetail/<int:pk>', views.JobDetail.as_view(), name='jobdetail'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
]
