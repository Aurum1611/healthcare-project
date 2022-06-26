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
    
    # Nested Endpoints
    path('patientcheckups/<int:pk>/', PatientDailyCheckupAPI.as_view()),
    path('patientcheckups/', PatientDailyCheckupAPI.as_view()),
    
    path('zonebaseddata/<int:zone_id>/', ZoneBasedDataAPI.as_view()),
    path('zonebaseddata/', ZoneBasedDataAPI.as_view()),
    
    path('locations/<int:pk>/', LocationAPI.as_view()),
    path('locations/', LocationAPI.as_view()),
    
    path('alltables/<int:pk>/', AllTablesAPI.as_view()),
    path('alltables/', AllTablesAPI.as_view()),
    
    path('allpatientchecks/<int:pk>/', AllPatientCheckupsAPI.as_view()),
    path('allpatientchecks/', AllPatientCheckupsAPI.as_view()),
]
