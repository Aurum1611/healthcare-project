from rest_framework import serializers
from .models import *


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ('id', 'name', 'code')    


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'name', 'code', 'zone')    


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'code', 'state')    


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('id', 'name', 'code', 'city', 'active')    


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'patient_unique_id', 'hospital', 'name',
                  'gender', 'dob', 'city', 'created_on', 'active')


class DoctorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorData
        fields = ('id', 'name', 'email_id', 'code',
                  'mobile_no', 'hospital', 'active')


class DailyCheckupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyCheckup
        fields = ('id', 'patient', 'height', 'weight',
                  'checkup_date', 'doctor_comment', 
                  'doctor', 'active')


class PatientDailyCheckupSerializer(serializers.ModelSerializer):
    
    patient = PatientSerializer()
    
    
    class Meta:
        model = DailyCheckup
        fields = ('id', 'patient', 'height', 'weight',
                  'checkup_date', 'doctor_comment', 
                  'doctor', 'active')


# API to get the data from Patient, DailyCheckup and Hospital based on Zone_id
class PatientHostpitalSerializer(serializers.ModelSerializer):
    
    hospital = HospitalSerializer()
    
    
    class Meta:
        model = Patient
        fields = ('id', 'patient_unique_id', 'hospital', 'name',
                  'gender', 'dob', 'city', 'created_on', 'active')


class ZoneBasedDataSerializer(serializers.ModelSerializer):
    
    patient = PatientHostpitalSerializer()
    
    
    class Meta:
        model = DailyCheckup
        fields = ('id', 'patient', 'height', 'weight',
                  'checkup_date', 'doctor_comment', 
                  'doctor', 'active')
