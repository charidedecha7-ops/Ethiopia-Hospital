from django.core.management.base import BaseCommand
from patients.models import Patient, MedicalHistory, Allergy
from doctors.models import Doctor
from core.models import User, Woreda
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Add sample patients with medical history and allergies'

    def handle(self, *args, **options):
        # Get admin user and woreda
        admin_user = User.objects.filter(is_superuser=True).first()
        woreda = Woreda.objects.first()
        doctors = Doctor.objects.all()[:3]
        
        if not admin_user:
            self.stdout.write(self.style.ERROR('No admin user found.'))
            return

        patients_data = [
            {
                'first_name': 'Marta',
                'last_name': 'Abera',
                'father_name': 'Abera Tadesse',
                'date_of_birth': date(1990, 5, 15),
                'gender': 'F',
                'blood_group': 'O+',
                'phone': '+251911234567',
                'email': 'marta.abera@email.com',
                'address': 'Addis Ababa, Bole',
                'kebele_id': 'KB-001-2024',
                'emergency_contact_name': 'Tadesse Abera',
                'emergency_contact_phone': '+251911234568',
            },
            {
                'first_name': 'Yohannes',
                'last_name': 'Kebede',
                'father_name': 'Kebede Tesfaye',
                'date_of_birth': date(1985, 8, 22),
                'gender': 'M',
                'blood_group': 'A+',
                'phone': '+251922345678',
                'email': 'yohannes.kebede@email.com',
                'address': 'Addis Ababa, Nifas Silk',
                'kebele_id': 'KB-002-2024',
                'emergency_contact_name': 'Tesfaye Kebede',
                'emergency_contact_phone': '+251922345679',
            },
            {
                'first_name': 'Hanna',
                'last_name': 'Solomon',
                'father_name': 'Solomon Girma',
                'date_of_birth': date(1992, 3, 10),
                'gender': 'F',
                'blood_group': 'B+',
                'phone': '+251933456789',
                'email': 'hanna.solomon@email.com',
                'address': 'Addis Ababa, Kolfe',
                'kebele_id': 'KB-003-2024',
                'emergency_contact_name': 'Girma Solomon',
                'emergency_contact_phone': '+251933456790',
            },
            {
                'first_name': 'Kebede',
                'last_name': 'Tadesse',
                'father_name': 'Tadesse Haile',
                'date_of_birth': date(1988, 11, 5),
                'gender': 'M',
                'blood_group': 'AB+',
                'phone': '+251944567890',
                'email': 'kebede.tadesse@email.com',
                'address': 'Addis Ababa, Yeka',
                'kebele_id': 'KB-004-2024',
                'emergency_contact_name': 'Haile Tadesse',
                'emergency_contact_phone': '+251944567891',
            },
            {
                'first_name': 'Almaz',
                'last_name': 'Bekele',
                'father_name': 'Bekele Assefa',
                'date_of_birth': date(1995, 7, 18),
                'gender': 'F',
                'blood_group': 'O-',
                'phone': '+251955678901',
                'email': 'almaz.bekele@email.com',
                'address': 'Addis Ababa, Lideta',
                'kebele_id': 'KB-005-2024',
                'emergency_contact_name': 'Assefa Bekele',
                'emergency_contact_phone': '+251955678902',
            },
        ]

        created_count = 0
        for patient_data in patients_data:
            if not Patient.objects.filter(phone=patient_data['phone']).exists():
                patient = Patient.objects.create(
                    first_name=patient_data['first_name'],
                    last_name=patient_data['last_name'],
                    father_name=patient_data['father_name'],
                    date_of_birth=patient_data['date_of_birth'],
                    gender=patient_data['gender'],
                    blood_group=patient_data['blood_group'],
                    phone=patient_data['phone'],
                    email=patient_data['email'],
                    woreda=woreda,
                    address=patient_data['address'],
                    kebele_id=patient_data['kebele_id'],
                    emergency_contact_name=patient_data['emergency_contact_name'],
                    emergency_contact_phone=patient_data['emergency_contact_phone'],
                    registered_by=admin_user,
                )
                
                # Add medical history
                if doctors:
                    doctor = doctors[created_count % len(doctors)]
                    MedicalHistory.objects.create(
                        patient=patient,
                        diagnosis='Initial Consultation',
                        symptoms='General checkup',
                        treatment='Routine examination',
                        doctor=doctor,
                        blood_pressure='120/80',
                        temperature=37.0,
                        heart_rate=72,
                        weight=70.0,
                        height=170.0,
                        glucose_level=95.0,
                    )
                
                # Add allergies
                if created_count % 2 == 0:
                    Allergy.objects.create(
                        patient=patient,
                        allergen='Penicillin',
                        reaction='Rash and itching',
                        severity='moderate',
                        diagnosed_date=date.today(),
                    )
                
                created_count += 1
                self.stdout.write(f"✓ {patient.patient_id} - {patient.full_name} ({patient.age} years)")

        self.stdout.write(self.style.SUCCESS(f"\n✓ {created_count} patients added successfully!"))
        
        # Display summary
        self.stdout.write("\n" + "="*60)
        self.stdout.write("Patients Summary:")
        self.stdout.write("="*60)
        self.stdout.write(f"Total Patients: {Patient.objects.count()}")
        self.stdout.write(f"Medical Histories: {MedicalHistory.objects.count()}")
        self.stdout.write(f"Allergies: {Allergy.objects.count()}")
