from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('DC', 'Design & Creative'),
    ('DD', 'Design & Developement'),
    ('SM', 'Sales & Marketing'),
    ('MA', 'Mobile Application'),
    ('CT', 'Construction'),
    ('IT', 'Information Technology'),
    ('RE', 'Real Estate'),
    ('CW', 'Content Writter'),
)

TIME_CHOICES = (
    ('TN', 'Temps Plein'),
    ('TP', 'Temps Partiel'),
    ('TP', 'Freelance'),
    ('TP', 'Remote'),
)


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_adress = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='company')
    company_email = models.EmailField()
    company_description = models.TextField()

    def __str__(self):
        return self.company_name

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    published_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    job_time = models.CharField(choices=TIME_CHOICES,max_length=2, blank=True)


    def _str_(self):
        return self.title 


class User(models.Model):
    username = models.CharField(max_length=100)




