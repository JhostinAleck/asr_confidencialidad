
from django.db import models

class PatientData(models.Model):
    patient_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    diagnosis = models.TextField()
    treatment = models.TextField()
    medical_history = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Patient {self.patient_id}: {self.name}"