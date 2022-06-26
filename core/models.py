from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True)


class State(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.DO_NOTHING, blank=True, null=True)


class City(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, blank=True, null=True)


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, blank=True, null=True)
    active = models.IntegerField(default=2)


class Patient(models.Model):
    patient_unique_id = models.CharField(max_length=200, unique=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    
    gender_choices = [
        (1, 'Male'), 
        (2, 'Female'),
    ]
    gender = models.IntegerField(choices=gender_choices, blank=True, null=True)
    
    dob = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField(default=2)

    @property
    def daily_checkups(self):
        return DailyCheckup.objects.filter(patient=self.id)


class DoctorData(models.Model):
    name = models.CharField(max_length=400)
    email_id = models.CharField(max_length=400, unique=True)
    code = models.CharField(max_length=400)
    mobile_no = models.CharField(max_length=12, unique=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING)
    active = models.IntegerField(default=2)


class DailyCheckup(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    height = models.FloatField(default=0.)
    weight = models.FloatField(default=0.)
    checkup_date = models.DateField(blank=True, null=True)
    doctor_comment = models.CharField(max_length=2500)
    doctor = models.ForeignKey(DoctorData, on_delete=models.DO_NOTHING)
    active = models.IntegerField(default=2)
