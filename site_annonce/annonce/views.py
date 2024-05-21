from django.shortcuts import render
from django.views import View

from .models import CATEGORY_CHOICES, Job

# Create your views here.
def base(request, *args, **kwargs):
    return render(request, "annonce/base.html", {})

def home(request, *args, **kwargs):
    return render(request, "annonce/home.html", {})

def about(request, *args, **kwargs):
    return render(request, "annonce/about.html", {})

def contact(request, *args, **kwargs):
    return render(request, "annonce/contact.html", {})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'annonce/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'job_detail.html', {'job': job})

class CategoryView(View):
 def get(self, request, val):
        jobs =Job.objects.filter(category=val) 
        return render(request, "annonce/job_list.html", locals())

def category_list(request):
        categories = dict(CATEGORY_CHOICES).get(category=val)
        return render(request, 'annonce/job_list.html', {'categories': CATEGORY_CHOICES})

class JobDetail(View):
 def get(self, request,pk):
    jobs=Job.objects.get(pk=pk)
    return render(request, 'annonce/job_detail.html', locals())
 

