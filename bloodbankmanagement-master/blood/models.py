from django.db import models
from django.utils.timezone import now
from patient import models as pmodels
from donor import models as dmodels

class Stock(models.Model):
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updates on save
    def __str__(self):
        return self.bloodgroup

class BloodRequest(models.Model):
    request_by_patient = models.ForeignKey(pmodels.Patient, null=True, on_delete=models.CASCADE)
    request_by_donor = models.ForeignKey(dmodels.Donor, null=True, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    patient_age = models.PositiveIntegerField()
    reason = models.CharField(max_length=500)
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="Pending")
    date = models.DateField(auto_now=True)
    created_at = models.DateTimeField(default=now)  # Add timestamp

    def __str__(self):
        return self.bloodgroup
