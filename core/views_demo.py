from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from doctors.models import Doctor
from patients.models import Patient
from pharmacy.models import Medicine
from laboratory.models import LabTest
from appointments.models import Appointment
from billing.models import Bill


@login_required
def demo_data(request):
    """Display all sample data"""
    context = {
        'doctors': Doctor.objects.all(),
        'patients': Patient.objects.all(),
        'medicines': Medicine.objects.all(),
        'lab_tests': LabTest.objects.all(),
        'appointments': Appointment.objects.all(),
        'bills': Bill.objects.all(),
    }
    return render(request, 'core/demo_data.html', context)
