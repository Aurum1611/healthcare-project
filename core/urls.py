from django.urls import path
from .views import *

urlpatterns = [
    # Endpoints
    path('zones/<int:pk>/', ZoneAPI.as_view()),
    path('zones/', ZoneAPI.as_view()),
    
    path('states/<int:pk>/', StateAPI.as_view()),
    path('states/', StateAPI.as_view()),
    
    path('cities/<int:pk>/', CityAPI.as_view()),
    path('cities/', CityAPI.as_view()),
    
    path('hospitals/<int:pk>/', HospitalAPI.as_view()),
    path('hospitals/', HospitalAPI.as_view()),
    
    path('patients/<int:pk>/', PatientAPI.as_view()),
    path('patients/', PatientAPI.as_view()),
    
    path('doctordata/<int:pk>/', DoctorDataAPI.as_view()),
    path('doctordata/', DoctorDataAPI.as_view()),
    
    path('dailycheckups/<int:pk>/', DailyCheckupAPI.as_view()),
    path('dailycheckups/', DailyCheckupAPI.as_view()),
]
