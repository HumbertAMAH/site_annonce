from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Company, Job


# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_adress', 'company_logo', 'company_email', 'company_description')
    search_fields = ('company_name', 'company_adress', 'company_logo')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'category', 'published_at', 'deadline')
    list_filter = ('category', 'published_at', 'deadline')
    search_fields = ('title', 'company__name', 'category__name')
