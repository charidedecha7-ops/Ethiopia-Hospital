from django.core.management.base import BaseCommand
from django.utils import timezone
from billing.models import Bill, BillItem, Payment
from patients.models import Patient
from appointments.models import Appointment
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Add sample bills and payments'

    def handle(self, *args, **options):
        patients = Patient.objects.all()[:5]
        
        if not patients:
            self.stdout.write(self.style.ERROR('No patients found.'))
            return

        bills_data = [
            {
                'items': [
                    {'description': 'Consultation Fee', 'quantity': 1, 'unit_price': 150.00},
                    {'description': 'Malaria Test (RDT)', 'quantity': 1, 'unit_price': 50.00},
                ],
                'status': 'paid',
                'payment_method': 'cash',
                'paid_amount': 200.00,
            },
            {
                'items': [
                    {'description': 'Consultation Fee', 'quantity': 1, 'unit_price': 180.00},
                    {'description': 'Blood Glucose Test', 'quantity': 1, 'unit_price': 75.00},
                    {'description': 'Medication (Metformin)', 'quantity': 1, 'unit_price': 120.00},
                ],
                'status': 'partial',
                'payment_method': 'card',
                'paid_amount': 200.00,
            },
            {
                'items': [
                    {'description': 'Consultation Fee', 'quantity': 1, 'unit_price': 250.00},
                    {'description': 'ECG Test', 'quantity': 1, 'unit_price': 200.00},
                    {'description': 'Medication (Aspirin)', 'quantity': 2, 'unit_price': 50.00},
                ],
                'status': 'paid',
                'payment_method': 'mobile',
                'paid_amount': 550.00,
            },
            {
                'items': [
                    {'description': 'Consultation Fee', 'quantity': 1, 'unit_price': 150.00},
                    {'description': 'TB Screening', 'quantity': 1, 'unit_price': 150.00},
                ],
                'status': 'pending',
                'payment_method': '',
                'paid_amount': 0.00,
            },
            {
                'items': [
                    {'description': 'Consultation Fee', 'quantity': 1, 'unit_price': 180.00},
                    {'description': 'Urinalysis', 'quantity': 1, 'unit_price': 40.00},
                    {'description': 'Medication (Antibiotics)', 'quantity': 1, 'unit_price': 200.00},
                ],
                'status': 'paid',
                'payment_method': 'insurance',
                'paid_amount': 420.00,
            },
        ]

        created_count = 0
        for i, bill_data in enumerate(bills_data):
            patient = patients[i % len(patients)]
            
            # Calculate total
            total_amount = sum(item['quantity'] * item['unit_price'] for item in bill_data['items'])
            
            # Create bill
            bill = Bill.objects.create(
                patient=patient,
                total_amount=total_amount,
                paid_amount=bill_data['paid_amount'],
                status=bill_data['status'],
                payment_method=bill_data['payment_method'],
                notes=f'Bill for {patient.full_name}',
            )
            
            # Add bill items
            for item in bill_data['items']:
                BillItem.objects.create(
                    bill=bill,
                    description=item['description'],
                    quantity=item['quantity'],
                    unit_price=item['unit_price'],
                )
            
            # Add payment if paid or partial
            if bill_data['paid_amount'] > 0:
                Payment.objects.create(
                    bill=bill,
                    amount=bill_data['paid_amount'],
                    payment_method=bill_data['payment_method'],
                    transaction_id=f'TXN-{bill.bill_id}',
                )
            
            created_count += 1
            self.stdout.write(f"✓ {bill.bill_id} - {patient.full_name} - {total_amount} ETB ({bill_data['status']})")

        self.stdout.write(self.style.SUCCESS(f"\n✓ {created_count} bills added successfully!"))
        
        # Display summary
        self.stdout.write("\n" + "="*60)
        self.stdout.write("Billing Summary:")
        self.stdout.write("="*60)
        
        for status in ['pending', 'partial', 'paid', 'cancelled']:
            count = Bill.objects.filter(status=status).count()
            total = sum(b.total_amount for b in Bill.objects.filter(status=status))
            self.stdout.write(f"{status.capitalize()}: {count} bills - {total} ETB")
        
        self.stdout.write(f"Total Bills: {Bill.objects.count()}")
        self.stdout.write(f"Total Revenue: {sum(b.total_amount for b in Bill.objects.all())} ETB")
