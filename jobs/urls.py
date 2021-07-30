from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home', ),
    path('about/', views.about, name='about'),
    path('job_search/', views.job_search, name='job_search'),
    path('contact/', views.contact, name='contact'),
    path('success', views.success, name='success'),
    path('apply/', views.apply, name='apply'),
    path('send_email/', views.send_email, name='send_email'),
]
