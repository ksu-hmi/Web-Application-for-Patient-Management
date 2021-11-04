rom django.db import models

# Create your models here.

# Table name would be drchrono_appointmentHistoryModel
class AppointmentHistoryModel(models.Model):
    # auto_now_add tells Django that when you add a new row (Patient Status), you want the current date & time added. 
    # auto_now tells Django that when a new row's record is saved (Patient Status), you want to add the current date & time.
    name=models.CharField(null=True, max_length=50)
    appointment_id = models.IntegerField()
    patient_id = models.IntegerField(null=True)
    statusTime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    appointment_start_time = models.DateTimeField(null=True)
    duration = models.IntegerField(null=True)
    session_start_time = models.DateTimeField(null=True)
    session_end_time = models.DateTimeField(null=True)
    check = models.BooleanField(default=False, max_length= 10)

    class Meta:
	    unique_together = ("appointment_id","appointment_start_time")
	    ordering = ['-statusTime']
   
