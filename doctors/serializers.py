from rest_framework import serializers
from .models import Doctor, Nurse
from core.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Doctor
        fields = [
            'id', 'user', 'full_name', 'license_number', 'specialization',
            'qualification', 'experience_years', 'consultation_fee',
            'available_days', 'available_time_start', 'available_time_end',
            'is_available', 'image', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
    
    def get_full_name(self, obj):
        return obj.user.get_full_name()

class DoctorCreateUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = Doctor
        fields = [
            'first_name', 'last_name', 'email', 'username', 'password',
            'license_number', 'specialization', 'qualification',
            'experience_years', 'consultation_fee', 'available_days',
            'available_time_start', 'available_time_end', 'is_available', 'image'
        ]
    
    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        email = validated_data.pop('email')
        username = validated_data.pop('username')
        password = validated_data.pop('password', 'doctor123')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True
        )
        
        doctor = Doctor.objects.create(user=user, **validated_data)
        return doctor
    
    def update(self, instance, validated_data):
        first_name = validated_data.pop('first_name', None)
        last_name = validated_data.pop('last_name', None)
        email = validated_data.pop('email', None)
        password = validated_data.pop('password', None)
        
        if first_name:
            instance.user.first_name = first_name
        if last_name:
            instance.user.last_name = last_name
        if email:
            instance.user.email = email
        if password:
            instance.user.set_password(password)
        instance.user.save()
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance

class NurseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Nurse
        fields = [
            'id', 'user', 'full_name', 'license_number', 'qualification',
            'department', 'shift', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
    
    def get_full_name(self, obj):
        return obj.user.get_full_name()
