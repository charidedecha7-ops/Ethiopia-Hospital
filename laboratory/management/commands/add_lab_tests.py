from django.core.management.base import BaseCommand
from django.utils import timezone
from laboratory.models import LabTest
from patients.models import Patient
from doctors.models import Doctor
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Add sample laboratory tests'

    def handle(self, *args, **options):
        # Get patients and doctors
        patients = Patient.objects.all()[:5]
        doctors = Doctor.objects.all()[:3]
        
        if not patients or not doctors:
            self.stdout.write(self.style.ERROR('No patients or doctors found. Run add_doctors first.'))
            return

        # Sample lab tests
        lab_tests_data = [
            {
                'test_name': 'Malaria Test (RDT)',
                'test_type': 'Rapid Diagnostic Test',
                'status': 'completed',
                'cost': 50.00,
                'malaria_test': 'positive',
                'results': 'Malaria parasite detected. Recommend artemether-lumefantrine treatment.',
            },
            {
                'test_name': 'Blood Glucose Test',
                'test_type': 'Fasting Blood Sugar',
                'status': 'completed',
                'cost': 75.00,
                'blood_glucose': 180.5,
                'results': 'Elevated blood glucose. Patient may have diabetes. Recommend further testing.',
            },
            {
                'test_name': 'Complete Blood Count (CBC)',
                'test_type': 'Hematology',
                'status': 'completed',
                'cost': 100.00,
                'hemoglobin': 12.5,
                'results': 'Hemoglobin level normal. No anemia detected.',
            },
            {
                'test_name': 'Typhoid Test',
                'test_type': 'Widal Test',
                'status': 'in_progress',
                'cost': 60.00,
                'results': 'Test in progress. Results expected within 24 hours.',
            },
            {
                'test_name': 'TB Screening',
                'test_type': 'Chest X-ray',
                'status': 'pending',
                'cost': 150.00,
                'results': 'Awaiting radiologist review.',
            },
            {
                'test_name': 'Malaria Test (RDT)',
                'test_type': 'Rapid Diagnostic Test',
                'status': 'completed',
                'cost': 50.00,
                'malaria_test': 'negative',
                'results': 'No malaria parasite detected.',
            },
            {
                'test_name': 'Blood Glucose Test',
                'test_type': 'Fasting Blood Sugar',
                'status': 'completed',
                'cost': 75.00,
                'blood_glucose': 95.0,
                'results': 'Blood glucose level normal.',
            },
            {
                'test_name': 'Urinalysis',
                'test_type': 'Urine Test',
                'status': 'completed',
                'cost': 40.00,
                'results': 'No abnormalities detected in urine sample.',
            },
        ]

        created_count = 0
        for i, test_data in enumerate(lab_tests_data):
            patient = patients[i % len(patients)]
            doctor = doctors[i % len(doctors)]
            
            # Check if test already exists
            if LabTest.objects.filter(
                patient=patient,
                test_name=test_data['test_name'],
                requested_date__date=timezone.now().date()
            ).exists():
                continue
            
            # Create lab test
            lab_test = LabTest.objects.create(
                patient=patient,
                doctor=doctor,
                test_name=test_data['test_name'],
                test_type=test_data['test_type'],
                status=test_data['status'],
                cost=test_data['cost'],
                malaria_test=test_data.get('malaria_test', ''),
                blood_glucose=test_data.get('blood_glucose'),
                hemoglobin=test_data.get('hemoglobin'),
                results=test_data['results'],
            )
            
            # Set completed date if completed
            if test_data['status'] == 'completed':
                lab_test.completed_date = timezone.now() - timedelta(hours=random.randint(1, 24))
                lab_test.save()
            
            created_count += 1
            self.stdout.write(f"✓ {lab_test.test_id} - {test_data['test_name']} ({test_data['status']})")

        self.stdout.write(self.style.SUCCESS(f"\n✓ {created_count} lab tests added successfully!"))
        
        # Display summary
        self.stdout.write("\n" + "="*60)
        self.stdout.write("Laboratory Tests Summary:")
        self.stdout.write("="*60)
        
        for status in ['pending', 'in_progress', 'completed', 'cancelled']:
            count = LabTest.objects.filter(status=status).count()
            self.stdout.write(f"{status.capitalize()}: {count}")
        
        self.stdout.write(f"Total Tests: {LabTest.objects.count()}")
