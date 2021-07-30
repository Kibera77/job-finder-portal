from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register_user/', views.register_user, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login_user.html'), name='login'),
    path('logout_user/', views.logout_user, name='logout'),

]
