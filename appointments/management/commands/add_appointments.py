from django.core.management.base import BaseCommand
from appointments.models import Appointment
from patients.models import Patient
from doctors.models import Doctor
from datetime import date, time, timedelta
import random

class Command(BaseCommand):
    help = 'Add sample appointments'

    def handle(self, *args, **options):
        patients = Patient.objects.all()[:5]
        doctors = Doctor.objects.all()[:3]
        
        if not patients or not doctors:
            self.stdout.write(self.style.ERROR('No patients or doctors found.'))
            return

        appointments_data = [
            {
                'appointment_date': date.today() + timedelta(days=1),
                'appointment_time': time(9, 0),
                'reason': 'Regular checkup',
                'status': 'scheduled',
                'distance_from_hospital': 5.5,
                'weather_condition': 'sunny',
                'sms_sent': True,
                'no_show_probability': 0.15,
            },
            {
                'appointment_date': date.today() + timedelta(days=2),
                'appointment_time': time(10, 30),
                'reason': 'Follow-up consultation',
                'status': 'confirmed',
                'distance_from_hospital': 12.0,
                'weather_condition': 'cloudy',
                'sms_sent': True,
                'no_show_probability': 0.25,
            },
            {
                'appointment_date': date.today() - timedelta(days=1),
                'appointment_time': time(14, 0),
                'reason': 'Lab test results review',
                'status': 'completed',
                'distance_from_hospital': 3.2,
                'weather_condition': 'sunny',
                'sms_sent': True,
                'no_show_probability': 0.05,
            },
            {
                'appointment_date': date.today() + timedelta(days=3),
                'appointment_time': time(11, 0),
                'reason': 'Diabetes management',
                'status': 'scheduled',
                'distance_from_hospital': 8.5,
                'weather_condition': 'rainy',
                'sms_sent': False,
                'no_show_probability': 0.45,
            },
            {
                'appointment_date': date.today() - timedelta(days=2),
                'appointment_time': time(15, 30),
                'reason': 'Hypertension check',
                'status': 'no_show',
                'distance_from_hospital': 15.0,
                'weather_condition': 'rainy',
                'sms_sent': True,
                'no_show_probability': 0.65,
            },
            {
                'appointment_date': date.today() + timedelta(days=4),
                'appointment_time': time(13, 0),
                'reason': 'Pediatric consultation',
                'status': 'scheduled',
                'distance_from_hospital': 2.0,
                'weather_condition': 'sunny',
                'sms_sent': True,
                'no_show_probability': 0.10,
            },
            {
                'appointment_date': date.today() - timedelta(days=3),
                'appointment_time': time(10, 0),
                'reason': 'Cardiac evaluation',
                'status': 'completed',
                'distance_from_hospital': 6.5,
                'weather_condition': 'cloudy',
                'sms_sent': True,
                'no_show_probability': 0.08,
            },
            {
                'appointment_date': date.today() + timedelta(days=5),
                'appointment_time': time(16, 0),
                'reason': 'General examination',
                'status': 'scheduled',
                'distance_from_hospital': 10.0,
                'weather_condition': 'sunny',
                'sms_sent': False,
                'no_show_probability': 0.30,
            },
        ]

        created_count = 0
        for i, apt_data in enumerate(appointments_data):
            patient = patients[i % len(patients)]
            doctor = doctors[i % len(doctors)]
            
            appointment = Appointment.objects.create(
                patient=patient,
                doctor=doctor,
                appointment_date=apt_data['appointment_date'],
                appointment_time=apt_data['appointment_time'],
                reason=apt_data['reason'],
                status=apt_data['status'],
                distance_from_hospital=apt_data['distance_from_hospital'],
                weather_condition=apt_data['weather_condition'],
                sms_sent=apt_data['sms_sent'],
                no_show_probability=apt_data['no_show_probability'],
            )
            
            created_count += 1
            self.stdout.write(f"✓ {appointment.appointment_id} - {patient.full_name} with Dr. {doctor.user.get_full_name()} ({apt_data['status']})")

        self.stdout.write(self.style.SUCCESS(f"\n✓ {created_count} appointments added successfully!"))
        
        # Display summary
        self.stdout.write("\n" + "="*60)
        self.stdout.write("Appointments Summary:")
        self.stdout.write("="*60)
        
        for status in ['scheduled', 'confirmed', 'completed', 'cancelled', 'no_show']:
            count = Appointment.objects.filter(status=status).count()
            self.stdout.write(f"{status.capitalize()}: {count}")
        
        self.stdout.write(f"Total Appointments: {Appointment.objects.count()}")
