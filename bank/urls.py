from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('apply/', views.apply_loan, name='apply_loan'),
    path('application/<str:application_id>/', views.application_result, name='application_result'),
]