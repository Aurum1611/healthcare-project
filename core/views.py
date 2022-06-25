from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView


class ZoneAPI(APIView):
    
    def get(self, request, pk=None, format=None):
        if pk:
            obj = Zone.objects.get(id=pk)
            serializer = ZoneSerializer(obj)
            return Response(serializer.data)
        else:
            objs = Zone.objects.all()
            serializer = ZoneSerializer(objs, many=True)
            return Response(serializer.data)
        
    def post(self, request, format=None):
        data = request.data
        
        obj = Zone.objects.create(**data)
        
        serializer = ZoneSerializer(obj)
        return Response(serializer.data)


class StateAPI(APIView):
    
    def get(self, request, pk=None, format=None):
        if pk:
            obj = State.objects.get(id=pk)
            serializer = StateSerializer(obj)
            return Response(serializer.data)
        else:
            objs = State.objects.all()
            serializer = StateSerializer(objs, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        
        zone = Zone.objects.get(id=data['zone'])
        del data['zone']
        
        obj = State.objects.create(**data, zone=zone)
        
        serializer = StateSerializer(obj)
        return Response(serializer.data)


class CityAPI(APIView):
    
    def get(self, request, pk=None, format=None):
        if pk:
            obj = City.objects.get(id=pk)
            serializer = CitySerializer(obj)
            return Response(serializer.data)
        else:
            objs = City.objects.all()
            serializer = CitySerializer(objs, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        
        st = State.objects.get(id=data['state'])
        del data['state']
        
        obj = City.objects.create(**data, state=st)
        
        serializer = CitySerializer(obj)
        return Response(serializer.data)


class HospitalAPI(APIView):
    
    def get(self, request, pk=None, format=None):
        if pk:
            obj = Hospital.objects.get(id=pk)
            serializer = HospitalSerializer(obj)
            return Response(serializer.data)
        else:
            objs = Hospital.objects.all()
            serializer = HospitalSerializer(objs, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        
        ct = City.objects.get(id=data['city'])
        del data['city']
        
        obj = Hospital.objects.create(**data, city=ct)
        
        serializer = HospitalSerializer(obj)
        return Response(serializer.data)


class PatientAPI(APIView):
    
    def get(self, request, pk=None, format=None):
        if pk:
            obj = Patient.objects.get(id=pk)
            serializer = PatientSerializer(obj)
            return Response(serializer.data)
        else:
            objs = Patient.objects.all()
            serializer = PatientSerializer(objs, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        
        hsp = Hospital.objects.get(id=data['hospital'])
        del data['hospital']
        
        obj = Patient.objects.create(**data, hospital=hsp)
        
        serializer = PatientSerializer(obj)
        return Response(serializer.data)


class DoctorDataAPI(APIView):
    
    def get(self, request, pk=None, format=None):
        if pk:
            obj = DoctorData.objects.get(id=pk)
            serializer = DoctorDataSerializer(obj)
            return Response(serializer.data)
        else:
            objs = DoctorData.objects.all()
            serializer = DoctorDataSerializer(objs, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        
        hsp = Hospital.objects.get(id=data['hospital'])
        del data['hospital']
        
        obj = DoctorData.objects.create(**data, hospital=hsp)
        
        serializer = DoctorDataSerializer(obj)
        return Response(serializer.data)


class DailyCheckupAPI(APIView):
    
    def get(self, request, pk=None, format=None):
        if pk:
            obj = DailyCheckup.objects.get(id=pk)
            serializer = DailyCheckupSerializer(obj)
            return Response(serializer.data)
        else:
            objs = DailyCheckup.objects.all()
            serializer = DailyCheckupSerializer(objs, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        
        doc = DoctorData.objects.get(id=data['doctor'])
        del data['doctor']
        
        pat = Patient.objects.get(id=data['patient'])
        del data['patient']
        
        obj = DailyCheckup.objects.create(**data, doctor=doc,
                                          patient=pat)
        
        serializer = DailyCheckupSerializer(obj)
        return Response(serializer.data)


class PatientDailyCheckupAPI(APIView):
    
    def get(self, request, pk=None, format=None):
        if pk:
            obj = DailyCheckup.objects.get(id=pk)
            serializer = PatientDailyCheckupSerializer(obj)
            return Response(serializer.data)
        else:
            objs = DailyCheckup.objects.all()
            serializer = PatientDailyCheckupSerializer(objs, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        
        doc = DoctorData.objects.get(id=data['doctor'])
        del data['doctor']
        
        patient_data = data['patient']
        del data['patient']
        
        pat = None
        if patient_data.get('id'):
            # update patient if any new data
            pat = Patient.objects.get(id=patient_data['id'])
            
            pat.patient_unique_id = patient_data.get('patient_unique_id', 
                                                 pat.patient_unique_id)
            pat.hospital = Hospital.objects.get(
                id=patient_data.get('hospital', pat.hospital.id)
            )
            pat.name = patient_data.get('name', pat.name)
            pat.gender = patient_data.get('gender', pat.gender)
            pat.dob = patient_data.get('dob', pat.dob)
            pat.city = patient_data.get('city', pat.city)
            pat.created_on = patient_data.get('created_on', pat.created_on)
            pat.active = patient_data.get('active', pat.active)
            pat.save()
        else:
            # create new patient
            hsp = Hospital.objects.get(id=patient_data['hospital'])
            del patient_data['hospital']
        
            pat = Patient.objects.create(**patient_data, hospital=hsp)
        
        # create new dailycheckup object
        obj = DailyCheckup.objects.create(**data, doctor=doc,
                                          patient=pat)
        
        serializer = DailyCheckupSerializer(obj)
        return Response(serializer.data)


# API to get the data from Patient, DailyCheckup and Hospital based on Zone_id
class ZoneBasedDataAPI(APIView):
    
    def get(self, request, zone_id=None, format=None):
        if zone_id:
            objs = DailyCheckup.objects.filter(
                patient__hospital__city__state__zone__id=zone_id
            )
            serializer = ZoneBasedDataSerializer(objs, many=True)
            return Response(serializer.data)
        else:
            objs = DailyCheckup.objects.all()
            serializer = ZoneBasedDataSerializer(objs, many=True)
            return Response(serializer.data)
