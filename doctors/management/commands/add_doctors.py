from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from core.models import User
from doctors.models import Doctor
from datetime import time
import os
from PIL import Image
from io import BytesIO

class Command(BaseCommand):
    help = 'Add multiple doctors with sample images'

    def handle(self, *args, **options):
        doctors_data = [
            {
                'first_name': 'Abebe',
                'last_name': 'Kebede',
                'email': 'abebe.kebede@hospital.et',
                'username': 'dr_abebe',
                'password': 'doctor123',
                'license_number': 'LIC-001',
                'specialization': 'general',
                'qualification': 'MD, Addis Ababa University',
                'experience_years': 8,
                'consultation_fee': 150.00,
                'available_days': 'Mon,Tue,Wed,Thu,Fri',
                'available_time_start': '09:00',
                'available_time_end': '17:00',
            },
            {
                'first_name': 'Tigist',
                'last_name': 'Haile',
                'email': 'tigist.haile@hospital.et',
                'username': 'dr_tigist',
                'password': 'doctor123',
                'license_number': 'LIC-002',
                'specialization': 'gynecology',
                'qualification': 'MD, Gynecology Specialist',
                'experience_years': 12,
                'consultation_fee': 200.00,
                'available_days': 'Mon,Tue,Wed,Thu,Fri,Sat',
                'available_time_start': '08:00',
                'available_time_end': '18:00',
            },
            {
                'first_name': 'Dawit',
                'last_name': 'Tesfaye',
                'email': 'dawit.tesfaye@hospital.et',
                'username': 'dr_dawit',
                'password': 'doctor123',
                'license_number': 'LIC-003',
                'specialization': 'cardiology',
                'qualification': 'MD, Cardiology Specialist',
                'experience_years': 15,
                'consultation_fee': 250.00,
                'available_days': 'Mon,Tue,Wed,Thu,Fri',
                'available_time_start': '10:00',
                'available_time_end': '16:00',
            },
            {
                'first_name': 'Almaz',
                'last_name': 'Girma',
                'email': 'almaz.girma@hospital.et',
                'username': 'dr_almaz',
                'password': 'doctor123',
                'license_number': 'LIC-004',
                'specialization': 'pediatrics',
                'qualification': 'MD, Pediatrics Specialist',
                'experience_years': 10,
                'consultation_fee': 180.00,
                'available_days': 'Mon,Tue,Wed,Thu,Fri,Sat',
                'available_time_start': '09:00',
                'available_time_end': '17:00',
            },
            {
                'first_name': 'Hanna',
                'last_name': 'Bekele',
                'email': 'hanna.bekele@hospital.et',
                'username': 'dr_hanna',
                'password': 'doctor123',
                'license_number': 'LIC-005',
                'specialization': 'surgery',
                'qualification': 'MD, Surgery Specialist',
                'experience_years': 18,
                'consultation_fee': 300.00,
                'available_days': 'Mon,Tue,Wed,Thu,Fri',
                'available_time_start': '08:00',
                'available_time_end': '16:00',
            },
        ]

        for doctor_info in doctors_data:
            # Create or get user
            user, created = User.objects.get_or_create(
                username=doctor_info['username'],
                defaults={
                    'first_name': doctor_info['first_name'],
                    'last_name': doctor_info['last_name'],
                    'email': doctor_info['email'],
                    'is_staff': True,
                }
            )
            
            if created:
                user.set_password(doctor_info['password'])
                user.save()
                self.stdout.write(f"✓ User {user.username} created")
            
            # Create or update doctor profile
            doctor, created = Doctor.objects.get_or_create(
                user=user,
                defaults={
                    'license_number': doctor_info['license_number'],
                    'specialization': doctor_info['specialization'],
                    'qualification': doctor_info['qualification'],
                    'experience_years': doctor_info['experience_years'],
                    'consultation_fee': doctor_info['consultation_fee'],
                    'available_days': doctor_info['available_days'],
                    'available_time_start': doctor_info['available_time_start'],
                    'available_time_end': doctor_info['available_time_end'],
                }
            )
            
            # Generate a sample image if not exists
            if not doctor.image:
                image = self.generate_sample_image(doctor_info['first_name'])
                doctor.image.save(
                    f"doctor_{doctor_info['username']}.jpg",
                    image,
                    save=True
                )
            
            status = "created" if created else "updated"
            self.stdout.write(
                self.style.SUCCESS(
                    f"✓ Dr. {user.get_full_name()} ({doctor_info['specialization']}) {status}"
                )
            )

        self.stdout.write(
            self.style.SUCCESS("\n✓ All doctors added successfully!")
        )

    def generate_sample_image(self, name):
        """Generate a simple colored image for the doctor"""
        img = Image.new('RGB', (200, 200), color=self.get_color_for_name(name))
        img_io = BytesIO()
        img.save(img_io, 'JPEG')
        img_io.seek(0)
        return ContentFile(img_io.getvalue(), name='doctor_image.jpg')

    def get_color_for_name(self, name):
        """Generate a consistent color based on name"""
        colors = [
            (52, 152, 219),    # Blue
            (46, 204, 113),    # Green
            (155, 89, 182),    # Purple
            (230, 126, 34),    # Orange
            (231, 76, 60),     # Red
        ]
        return colors[hash(name) % len(colors)]
