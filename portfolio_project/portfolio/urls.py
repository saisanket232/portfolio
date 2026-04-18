from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/soilguard/', views.soilguard, name='soilguard'),
    path('projects/finance/', views.finance, name='finance'),
    path('experience/', views.experience, name='experience'),
    path('experience/intern/', views.experience_detail, name='experience_detail'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact'),
]