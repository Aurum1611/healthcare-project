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
    
    BMI_results = serializers.SerializerMethodField()
    
    
    class Meta:
        model = DailyCheckup
        fields = ('id', 'patient', 'height', 'weight', 'BMI', 'BMI_results',
                  'checkup_date','doctor_comment', 'doctor', 'active')
    
    def get_BMI_results(self, obj):
        return obj.find_BMI_results()


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


# Api Zone, State and City
class RegionSerializer(serializers.ModelSerializer):
    
    zone = ZoneSerializer()
    
    
    class Meta:
        model = State
        fields = ('id', 'name', 'code', 'zone')    


class LocationSerializer(serializers.ModelSerializer):
    
    state = RegionSerializer()
    
    
    class Meta:
        model = City
        fields = ('id', 'name', 'code', 'state')


# Using a single Api create a new entry in all the above tables
class HospitalLocationSerializer(serializers.ModelSerializer):
    
    city = LocationSerializer()
    
    
    class Meta:
        model = Hospital
        fields = ('id', 'name', 'code', 'city', 'active')    


class PatientSuperSerializer(serializers.ModelSerializer):
    
    hospital = HospitalLocationSerializer()
    
    
    class Meta:
        model = Patient
        fields = ('id', 'patient_unique_id', 'hospital', 'name',
                  'gender', 'dob', 'city', 'created_on', 'active')


class DoctorSuperSerializer(serializers.ModelSerializer):
    
    hospital = HospitalLocationSerializer()
    
    
    class Meta:
        model = DoctorData
        fields = ('id', 'name', 'email_id', 'code',
                  'mobile_no', 'hospital', 'active')


class AllTablesSerializer(serializers.ModelSerializer):
    
    patient = PatientSuperSerializer()
    doctor = DoctorSuperSerializer()
    
    class Meta:
        model = DailyCheckup
        fields = ('id', 'patient', 'height', 'weight',
                  'checkup_date', 'doctor_comment', 
                  'doctor', 'active')


# API to get patient data along with all daily_checkups of that patient
class AllPatientCheckupsSerializer(serializers.ModelSerializer):
    
    daily_checkups = DailyCheckupSerializer(many=True)
    
    
    class Meta:
        model = Patient
        fields = ('id', 'patient_unique_id', 'hospital', 'name', 'gender',
                  'dob', 'daily_checkups', 'city', 'created_on', 'active')
