from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    url(r'^login/', views.loginview, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='app/home.html'), name='logout'),
    url(r'blogs/$', views.GetBlogs, name='blogs'),
    url(r'workouts/$', views.GetWorkoutPlans, name='workouts'),
    
]
