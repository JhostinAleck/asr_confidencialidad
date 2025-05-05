from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import PatientData
from .serializers import PatientDataSerializer
import logging

logger = logging.getLogger(__name__)

class PatientDataViewSet(viewsets.ModelViewSet):
    queryset = PatientData.objects.all()
    serializer_class = PatientDataSerializer
    
    def create(self, request, *args, **kwargs):
        logger.info("Recibiendo solicitud PUT para crear datos de paciente")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        logger.info(f"Datos de paciente creados exitosamente: ID {serializer.data['id']}")
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        logger.info(f"Recibiendo solicitud PUT para actualizar datos de paciente: ID {kwargs.get('pk')}")
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        logger.info(f"Datos de paciente actualizados exitosamente: ID {kwargs.get('pk')}")
        return Response(serializer.data)