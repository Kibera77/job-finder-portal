import django_filters

from .models import *


class JobFilter(django_filters.FilterSet):
    class Meta:
        model = JobPost
        fields = '__all__'
        exclude = ['job_name', 'company_name', 'pricing', 'thumbnail', ]
