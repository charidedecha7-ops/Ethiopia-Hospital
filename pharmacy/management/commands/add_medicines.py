from django.core.management.base import BaseCommand
from django.utils import timezone
from pharmacy.models import Medicine, Prescription, PrescriptionItem
from patients.models import Patient
from doctors.models import Doctor
from datetime import timedelta, date

class Command(BaseCommand):
    help = 'Add sample medicines and prescriptions'

    def handle(self, *args, **options):
        patients = Patient.objects.all()[:5]
        doctors = Doctor.objects.all()[:3]
        
        if not patients or not doctors:
            self.stdout.write(self.style.ERROR('No patients or doctors found.'))
            return

        # Sample medicines
        medicines_data = [
            {
                'name': 'Artemether-Lumefantrine',
                'generic_name': 'Artemether + Lumefantrine',
                'manufacturer': 'Novartis',
                'category': 'Antimalarial',
                'unit': 'tablet',
                'quantity': 500,
                'reorder_level': 100,
                'unit_price': 25.00,
                'expiry_date': date.today() + timedelta(days=365),
            },
            {
                'name': 'Metformin',
                'generic_name': 'Metformin HCl',
                'manufacturer': 'Cipla',
                'category': 'Antidiabetic',
                'unit': 'tablet',
                'quantity': 300,
                'reorder_level': 50,
                'unit_price': 15.00,
                'expiry_date': date.today() + timedelta(days=365),
            },
            {
                'name': 'Aspirin',
                'generic_name': 'Acetylsalicylic Acid',
                'manufacturer': 'Bayer',
                'category': 'Analgesic',
                'unit': 'tablet',
                'quantity': 1000,
                'reorder_level': 200,
                'unit_price': 5.00,
                'expiry_date': date.today() + timedelta(days=365),
            },
            {
                'name': 'Amoxicillin',
                'generic_name': 'Amoxicillin Trihydrate',
                'manufacturer': 'GSK',
                'category': 'Antibiotic',
                'unit': 'capsule',
                'quantity': 400,
                'reorder_level': 100,
                'unit_price': 20.00,
                'expiry_date': date.today() + timedelta(days=365),
            },
            {
                'name': 'Paracetamol',
                'generic_name': 'Acetaminophen',
                'manufacturer': 'Sanofi',
                'category': 'Analgesic',
                'unit': 'tablet',
                'quantity': 800,
                'reorder_level': 150,
                'unit_price': 3.00,
                'expiry_date': date.today() + timedelta(days=365),
            },
            {
                'name': 'Chloroquine',
                'generic_name': 'Chloroquine Phosphate',
                'manufacturer': 'Ipca',
                'category': 'Antimalarial',
                'unit': 'tablet',
                'quantity': 200,
                'reorder_level': 50,
                'unit_price': 10.00,
                'expiry_date': date.today() + timedelta(days=365),
            },
            {
                'name': 'Lisinopril',
                'generic_name': 'Lisinopril',
                'manufacturer': 'Merck',
                'category': 'Antihypertensive',
                'unit': 'tablet',
                'quantity': 250,
                'reorder_level': 50,
                'unit_price': 30.00,
                'expiry_date': date.today() + timedelta(days=365),
            },
            {
                'name': 'Omeprazole',
                'generic_name': 'Omeprazole',
                'manufacturer': 'AstraZeneca',
                'category': 'Antacid',
                'unit': 'capsule',
                'quantity': 350,
                'reorder_level': 75,
                'unit_price': 18.00,
                'expiry_date': date.today() + timedelta(days=365),
            },
        ]

        # Add medicines
        created_medicines = 0
        for med_data in medicines_data:
            if not Medicine.objects.filter(name=med_data['name']).exists():
                Medicine.objects.create(**med_data)
                created_medicines += 1
                self.stdout.write(f"✓ {med_data['name']} - {med_data['quantity']} {med_data['unit']}")

        self.stdout.write(self.style.SUCCESS(f"\n✓ {created_medicines} medicines added!"))

        # Sample prescriptions
        medicines = Medicine.objects.all()[:8]
        prescriptions_data = [
            {
                'diagnosis': 'Malaria',
                'items': [
                    {'medicine': medicines[0], 'dosage': '1 tablet', 'frequency': 'Twice daily', 'duration': '3 days', 'quantity': 6},
                ],
                'status': 'dispensed',
            },
            {
                'diagnosis': 'Type 2 Diabetes',
                'items': [
                    {'medicine': medicines[1], 'dosage': '500mg', 'frequency': 'Twice daily', 'duration': '30 days', 'quantity': 60},
                ],
                'status': 'dispensed',
            },
            {
                'diagnosis': 'Hypertension',
                'items': [
                    {'medicine': medicines[6], 'dosage': '10mg', 'frequency': 'Once daily', 'duration': '30 days', 'quantity': 30},
                ],
                'status': 'dispensed',
            },
            {
                'diagnosis': 'Bacterial Infection',
                'items': [
                    {'medicine': medicines[3], 'dosage': '500mg', 'frequency': 'Three times daily', 'duration': '7 days', 'quantity': 21},
                ],
                'status': 'pending',
            },
            {
                'diagnosis': 'Fever & Pain',
                'items': [
                    {'medicine': medicines[4], 'dosage': '500mg', 'frequency': 'Every 6 hours', 'duration': '5 days', 'quantity': 20},
                    {'medicine': medicines[2], 'dosage': '1 tablet', 'frequency': 'Once daily', 'duration': '5 days', 'quantity': 5},
                ],
                'status': 'dispensed',
            },
        ]

        # Add prescriptions
        created_prescriptions = 0
        for i, pre_data in enumerate(prescriptions_data):
            patient = patients[i % len(patients)]
            doctor = doctors[i % len(doctors)]
            
            prescription = Prescription.objects.create(
                patient=patient,
                doctor=doctor,
                diagnosis=pre_data['diagnosis'],
                status=pre_data['status'],
                notes=f'Prescription for {pre_data["diagnosis"]}',
            )
            
            # Add prescription items
            for item in pre_data['items']:
                PrescriptionItem.objects.create(
                    prescription=prescription,
                    medicine=item['medicine'],
                    dosage=item['dosage'],
                    frequency=item['frequency'],
                    duration=item['duration'],
                    quantity=item['quantity'],
                )
            
            created_prescriptions += 1
            self.stdout.write(f"✓ {prescription.prescription_id} - {pre_data['diagnosis']} ({pre_data['status']})")

        self.stdout.write(self.style.SUCCESS(f"\n✓ {created_prescriptions} prescriptions added!"))
        
        # Display summary
        self.stdout.write("\n" + "="*60)
        self.stdout.write("Pharmacy Summary:")
        self.stdout.write("="*60)
        self.stdout.write(f"Total Medicines: {Medicine.objects.count()}")
        self.stdout.write(f"Total Prescriptions: {Prescription.objects.count()}")
        
        for status in ['pending', 'dispensed', 'cancelled']:
            count = Prescription.objects.filter(status=status).count()
            self.stdout.write(f"Prescriptions ({status}): {count}")
        
        low_stock = Medicine.objects.filter(quantity__lt=50)
        self.stdout.write(f"Low Stock Items: {low_stock.count()}")
