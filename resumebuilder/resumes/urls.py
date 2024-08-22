from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.resume_form, name='resume_form'),
    path('preview/', views.preview_resume, name='preview'),
    path('download_pdf/', views.download_pdf, name='download_pdf'),
    path('resume-templates/', views.resume_templates, name='resume_templates'),
]

