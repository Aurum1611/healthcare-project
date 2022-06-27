from django.contrib import admin
from .models import *


class ZoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code') 


class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'zone')


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'state')


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'city', 'active')


class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_unique_id', 'hospital', 'name',
                  'gender', 'dob', 'city', 'created_on', 'active')
    search_fields = ('name',)
    list_filter = ('gender', 'active', 'hospital__name',)


class DoctorDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email_id', 'code', 
                    'mobile_no', 'hospital', 'active')
    search_fields = ('name', 'email_id',)


class DailyCheckupAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'height', 'weight', 'BMI', 
                    'checkup_date', 'doctor', 'active')
    exclude = ('doctor_comment',)


admin.site.register(Zone, ZoneAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(DoctorData, DoctorDataAdmin)
admin.site.register(DailyCheckup, DailyCheckupAdmin)
