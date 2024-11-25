from django.urls import path

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('logout', LogoutView.as_view(template_name='blood/logout.html'),name='logout'),
    path('patientlogin', LoginView.as_view(template_name='patient/patientlogin.html'),name='patientlogin'),
    path('patientsignup', views.patient_signup_view,name='patientsignup'),
    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('make-request', views.make_request_view,name='make-request'),
    path('my-request', views.my_request_view,name='my-request'),
]