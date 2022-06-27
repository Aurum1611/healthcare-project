from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name


class State(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, blank=True, null=True)
    active = models.IntegerField(default=2)

    def __str__(self) -> str:
        return self.name


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

    def __str__(self) -> str:
        return self.name
    
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

    def __str__(self) -> str:
        return self.name


class DailyCheckup(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    height = models.FloatField(default=0.)
    weight = models.FloatField(default=0.)
    checkup_date = models.DateField(blank=True, null=True)
    doctor_comment = models.CharField(max_length=2500)
    doctor = models.ForeignKey(DoctorData, on_delete=models.DO_NOTHING)
    active = models.IntegerField(default=2)
    
    @property
    def BMI(self):
        if self.weight and self.height:
            return self.weight / (self.height/100)**2
        else:
            return "BMI calculation requires non-zero weight and height."
    
    def find_BMI_results(self):
        if self.BMI <= 18.4: 
            return  "You are underweight." 
        elif self.BMI <= 24.9: 
            return "You are healthy." 
        elif self.BMI <= 29.9: 
            return "You are over weight." 
        elif self.BMI <= 34.9: 
            return "You are severely over weight." 
        elif self.BMI <= 39.9: 
            return "You are obese." 
        else: 
            return "You are severely obese."
