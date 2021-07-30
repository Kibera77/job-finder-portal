from django.contrib import admin
from django.contrib.auth.models import Group
from .models import JobPost, Employees


# Register your models here.

class JobPostAdmin(admin.ModelAdmin):
    list_display = ['job_name','company_name', 'pricing', 'category', 'location', 'experience']
    list_filter = ['category']


admin.site.site_header = 'Admin Dashboard'
admin.site.site_title = 'JobFinder site administration'
admin.site.index_title = 'JobFinder site administration'
admin.site.register(JobPost, JobPostAdmin)
admin.site.register(Employees)
# admin.site.unregister(Group)
