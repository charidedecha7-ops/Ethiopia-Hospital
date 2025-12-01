from django.core.management.base import BaseCommand
from doctors.models import Doctor
from core.models import User

class Command(BaseCommand):
    help = 'Remove duplicate doctors and keep only one of each'

    def handle(self, *args, **options):
        # Get all doctors
        doctors = Doctor.objects.all().select_related('user').order_by('user__username', '-image')
        
        # Track seen doctors by username
        seen = {}
        duplicates = []
        
        for doctor in doctors:
            username = doctor.user.username
            if username in seen:
                duplicates.append(doctor)
            else:
                seen[username] = doctor
        
        if duplicates:
            self.stdout.write(f"Found {len(duplicates)} duplicate doctor(s)")
            for doctor in duplicates:
                user = doctor.user
                self.stdout.write(f"Removing: Dr. {user.get_full_name()} ({user.username}) - {doctor.get_specialization_display()}")
                # Delete the doctor profile
                doctor.delete()
                # Delete the user
                user.delete()
            self.stdout.write(self.style.SUCCESS(f"✓ Removed {len(duplicates)} duplicate(s)"))
        else:
            self.stdout.write(self.style.SUCCESS("✓ No duplicates found"))
        
        # List remaining doctors
        self.stdout.write("\n" + "="*50)
        self.stdout.write("Remaining Doctors:")
        self.stdout.write("="*50)
        remaining = Doctor.objects.all().select_related('user')
        for i, doctor in enumerate(remaining, 1):
            has_image = "✓" if doctor.image else "✗"
            self.stdout.write(
                f"{i}. Dr. {doctor.user.get_full_name()} - {doctor.get_specialization_display()} [{has_image}]"
            )
