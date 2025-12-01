from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Doctor, Nurse
from .serializers import DoctorSerializer, DoctorCreateUpdateSerializer, NurseSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().select_related('user')
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return DoctorCreateUpdateSerializer
        return DoctorSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get all available doctors"""
        doctors = Doctor.objects.filter(is_available=True).select_related('user')
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_specialization(self, request):
        """Get doctors by specialization"""
        specialization = request.query_params.get('specialization')
        if not specialization:
            return Response(
                {'error': 'specialization parameter required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        doctors = Doctor.objects.filter(
            specialization=specialization,
            is_available=True
        ).select_related('user')
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def upload_image(self, request, pk=None):
        """Upload doctor image"""
        doctor = self.get_object()
        
        if 'image' not in request.FILES:
            return Response(
                {'error': 'No image file provided'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        doctor.image = request.FILES['image']
        doctor.save()
        
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all().select_related('user')
    serializer_class = NurseSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
