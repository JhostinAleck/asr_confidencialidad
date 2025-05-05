from rest_framework import serializers
from .models import PatientData

class PatientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientData
        fields = ['id', 'patient_id', 'name', 'diagnosis', 'treatment', 'medical_history']