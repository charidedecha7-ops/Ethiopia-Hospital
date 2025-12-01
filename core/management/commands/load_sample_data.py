from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import User
from doctors.models import Doctor
from patients.models import Patient
from laboratory.models import LabTest
from pharmacy.models import Medicine
from billing.models import Bill
from appointments.models import Appointment
from datetime import datetime, timedelta, date, time
import random


class Command(BaseCommand):
    help = 'Load sample data for Haramaya University Health Center'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n' + '='*70))
        self.stdout.write(self.style.SUCCESS('🏥 LOADING SAMPLE DATA'))
        self.stdout.write(self.style.SUCCESS('='*70 + '\n'))

        self.load_doctors()
        self.load_patients()
        self.load_medicines()
        self.load_lab_tests()
        self.load_appointments()
        self.load_bills()

        self.stdout.write(self.style.SUCCESS('\n' + '='*70))
        self.stdout.write(self.style.SUCCESS('✅ ALL DATA LOADED SUCCESSFULLY!'))
        self.stdout.write(self.style.SUCCESS('='*70))
        self.stdout.write(self.style.SUCCESS(f'\n👨‍⚕️  Doctors: {Doctor.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'👥 Patients: {Patient.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'💊 Medicines: {Medicine.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'🧪 Lab Tests: {LabTest.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'📅 Appointments: {Appointment.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'💰 Bills: {Bill.objects.count()}'))
        self.stdout.write(self.style.SUCCESS('\n🌐 Access: http://127.0.0.1:8000'))
        self.stdout.write(self.style.SUCCESS('🔐 Admin: admin / admin123'))
        self.stdout.write(self.style.SUCCESS('='*70 + '\n'))

    def load_doctors(self):
        self.stdout.write('\n👨‍⚕️ Loading Doctors...')
        
        doctors_data = [
            {
                'first_name': 'Abebe',
                'last_name': 'Kebede',
                'email': 'dr.abebe@haramaya.edu.et',
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
                'email': 'dr.tigist@haramaya.edu.et',
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
                'email': 'dr.dawit@haramaya.edu.et',
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
                'email': 'dr.almaz@haramaya.edu.et',
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
                'email': 'dr.hanna@haramaya.edu.et',
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
            user, created = User.objects.get_or_create(
                username=doctor_info['username'],
                defaults={
                    'first_name': doctor_info['first_name'],
                    'last_name': doctor_info['last_name'],
                    'email': doctor_info['email'],
                    'role': 'doctor',
                    'is_staff': True,
                }
            )
            
            if created:
                user.set_password(doctor_info['password'])
                user.save()
            
            Doctor.objects.get_or_create(
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
            self.stdout.write(f'  ✓ Dr. {doctor_info["first_name"]} {doctor_info["last_name"]}')

    def load_patients(self):
        self.stdout.write('\n👥 Loading Patients...')
        
        patients_data = [
            {
                'first_name': 'Yohannes',
                'last_name': 'Tadesse',
                'father_name': 'Tadesse Abebe',
                'phone': '+251911234567',
                'email': 'yohannes@student.haramaya.edu.et',
                'date_of_birth': '2002-05-15',
                'gender': 'M',
                'blood_group': 'O+',
                'kebele_id': 'KEB-001',
                'address': 'Haramaya Campus',
                'emergency_contact_name': 'Abebe Tadesse',
                'emergency_contact_phone': '+251911111111',
            },
            {
                'first_name': 'Marta',
                'last_name': 'Getnet',
                'father_name': 'Getnet Haile',
                'phone': '+251922345678',
                'email': 'marta@student.haramaya.edu.et',
                'date_of_birth': '2003-08-22',
                'gender': 'F',
                'blood_group': 'A+',
                'kebele_id': 'KEB-002',
                'address': 'Haramaya Campus',
                'emergency_contact_name': 'Haile Getnet',
                'emergency_contact_phone': '+251922222222',
            },
            {
                'first_name': 'Kedir',
                'last_name': 'Ahmed',
                'father_name': 'Ahmed Hassan',
                'phone': '+251933456789',
                'email': 'kedir@student.haramaya.edu.et',
                'date_of_birth': '2001-12-10',
                'gender': 'M',
                'blood_group': 'B+',
                'kebele_id': 'KEB-003',
                'address': 'Haramaya Campus',
                'emergency_contact_name': 'Hassan Ahmed',
                'emergency_contact_phone': '+251933333333',
            },
            {
                'first_name': 'Selam',
                'last_name': 'Abebe',
                'father_name': 'Abebe Lemma',
                'phone': '+251944567890',
                'email': 'selam@student.haramaya.edu.et',
                'date_of_birth': '2002-03-18',
                'gender': 'F',
                'blood_group': 'AB+',
                'kebele_id': 'KEB-004',
                'address': 'Haramaya Campus',
                'emergency_contact_name': 'Lemma Abebe',
                'emergency_contact_phone': '+251944444444',
            },
            {
                'first_name': 'Biruk',
                'last_name': 'Lemma',
                'father_name': 'Lemma Bekele',
                'phone': '+251955678901',
                'email': 'biruk@student.haramaya.edu.et',
                'date_of_birth': '2003-07-25',
                'gender': 'M',
                'blood_group': 'O-',
                'kebele_id': 'KEB-005',
                'address': 'Haramaya Campus',
                'emergency_contact_name': 'Bekele Lemma',
                'emergency_contact_phone': '+251955555555',
            },
            {
                'first_name': 'Zainab',
                'last_name': 'Hassan',
                'father_name': 'Hassan Mohammed',
                'phone': '+251966789012',
                'email': 'zainab@student.haramaya.edu.et',
                'date_of_birth': '2002-11-30',
                'gender': 'F',
                'blood_group': 'B-',
                'kebele_id': 'KEB-006',
                'address': 'Haramaya Campus',
                'emergency_contact_name': 'Mohammed Hassan',
                'emergency_contact_phone': '+251966666666',
            },
        ]

        for patient_info in patients_data:
            Patient.objects.get_or_create(
                email=patient_info['email'],
                defaults={
                    'first_name': patient_info['first_name'],
                    'last_name': patient_info['last_name'],
                    'father_name': patient_info['father_name'],
                    'phone': patient_info['phone'],
                    'date_of_birth': patient_info['date_of_birth'],
                    'gender': patient_info['gender'],
                    'blood_group': patient_info['blood_group'],
                    'kebele_id': patient_info['kebele_id'],
                    'address': patient_info['address'],
                    'emergency_contact_name': patient_info['emergency_contact_name'],
                    'emergency_contact_phone': patient_info['emergency_contact_phone'],
                }
            )
            self.stdout.write(f'  ✓ {patient_info["first_name"]} {patient_info["last_name"]}')

    def load_medicines(self):
        self.stdout.write('\n💊 Loading Medicines...')
        
        medicines_data = [
            {'name': 'Paracetamol 500mg', 'generic_name': 'Acetaminophen', 'quantity': 500, 'unit_price': 5.00, 'manufacturer': 'Addis Pharma', 'category': 'Analgesic'},
            {'name': 'Amoxicillin 250mg', 'generic_name': 'Amoxicillin', 'quantity': 300, 'unit_price': 15.00, 'manufacturer': 'Addis Pharma', 'category': 'Antibiotic'},
            {'name': 'Ibuprofen 400mg', 'generic_name': 'Ibuprofen', 'quantity': 400, 'unit_price': 8.00, 'manufacturer': 'Addis Pharma', 'category': 'NSAID'},
            {'name': 'Metformin 500mg', 'generic_name': 'Metformin', 'quantity': 200, 'unit_price': 12.00, 'manufacturer': 'Addis Pharma', 'category': 'Antidiabetic'},
            {'name': 'Lisinopril 10mg', 'generic_name': 'Lisinopril', 'quantity': 150, 'unit_price': 20.00, 'manufacturer': 'Addis Pharma', 'category': 'Antihypertensive'},
            {'name': 'Omeprazole 20mg', 'generic_name': 'Omeprazole', 'quantity': 250, 'unit_price': 10.00, 'manufacturer': 'Addis Pharma', 'category': 'Antacid'},
            {'name': 'Ciprofloxacin 500mg', 'generic_name': 'Ciprofloxacin', 'quantity': 100, 'unit_price': 25.00, 'manufacturer': 'Addis Pharma', 'category': 'Antibiotic'},
            {'name': 'Vitamin C 1000mg', 'generic_name': 'Ascorbic Acid', 'quantity': 600, 'unit_price': 3.00, 'manufacturer': 'Addis Pharma', 'category': 'Vitamin'},
            {'name': 'Aspirin 100mg', 'generic_name': 'Acetylsalicylic Acid', 'quantity': 400, 'unit_price': 4.00, 'manufacturer': 'Addis Pharma', 'category': 'Antiplatelet'},
            {'name': 'Cough Syrup', 'generic_name': 'Dextromethorphan', 'quantity': 200, 'unit_price': 18.00, 'manufacturer': 'Addis Pharma', 'category': 'Cough Suppressant'},
        ]

        expiry_date = date.today() + timedelta(days=365)
        
        for med in medicines_data:
            Medicine.objects.get_or_create(
                name=med['name'],
                defaults={
                    'generic_name': med['generic_name'],
                    'quantity': med['quantity'],
                    'unit_price': med['unit_price'],
                    'manufacturer': med['manufacturer'],
                    'category': med['category'],
                    'expiry_date': expiry_date,
                    'unit': 'tablet',
                }
            )
            self.stdout.write(f'  ✓ {med["name"]}')

    def load_lab_tests(self):
        self.stdout.write('\n🧪 Loading Laboratory Tests...')
        
        patients = list(Patient.objects.all())
        doctors = list(Doctor.objects.all())
        
        if not patients or not doctors:
            self.stdout.write(self.style.WARNING('  ⚠ Need patients and doctors first'))
            return
        
        tests_data = [
            {'test_name': 'Complete Blood Count', 'test_type': 'CBC', 'cost': 100.00},
            {'test_name': 'Malaria Test', 'test_type': 'RDT', 'cost': 50.00},
            {'test_name': 'Typhoid Test', 'test_type': 'Serology', 'cost': 75.00},
            {'test_name': 'HIV Test', 'test_type': 'Antibody', 'cost': 150.00},
            {'test_name': 'Glucose Test', 'test_type': 'Blood', 'cost': 40.00},
        ]

        for i, test in enumerate(tests_data):
            patient = patients[i % len(patients)]
            doctor = doctors[i % len(doctors)]
            
            LabTest.objects.get_or_create(
                patient=patient,
                test_name=test['test_name'],
                defaults={
                    'doctor': doctor,
                    'test_type': test['test_type'],
                    'cost': test['cost'],
                    'status': 'completed',
                    'results': f'Sample results for {test["test_name"]}',
                }
            )
            self.stdout.write(f'  ✓ {test["test_name"]}')

    def load_appointments(self):
        self.stdout.write('\n📅 Loading Appointments...')
        
        doctors = list(Doctor.objects.all())
        patients = list(Patient.objects.all())
        
        if not doctors or not patients:
            self.stdout.write(self.style.WARNING('  ⚠ Need doctors and patients first'))
            return
        
        reasons = ['Checkup', 'Follow-up', 'Consultation', 'Treatment']
        appointment_times = [time(9, 0), time(10, 30), time(14, 0), time(15, 30)]
        
        for i in range(5):
            appointment_date = datetime.now().date() + timedelta(days=random.randint(1, 30))
            appointment_time = random.choice(appointment_times)
            
            Appointment.objects.get_or_create(
                patient=patients[i % len(patients)],
                doctor=doctors[i % len(doctors)],
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                defaults={
                    'reason': random.choice(reasons),
                    'status': 'scheduled',
                    'notes': 'Sample appointment',
                }
            )
            self.stdout.write(f'  ✓ Appointment {i+1}')

    def load_bills(self):
        self.stdout.write('\n💰 Loading Bills...')
        
        patients = list(Patient.objects.all())[:3]
        
        if not patients:
            self.stdout.write(self.style.WARNING('  ⚠ Need patients first'))
            return
        
        for i, patient in enumerate(patients):
            total_amount = random.choice([500, 750, 1000])
            
            Bill.objects.get_or_create(
                patient=patient,
                defaults={
                    'total_amount': total_amount,
                    'paid_amount': total_amount,
                    'status': 'paid',
                    'payment_method': 'cash',
                    'notes': 'Sample bill',
                }
            )
            self.stdout.write(f'  ✓ Bill for {patient.first_name}')
