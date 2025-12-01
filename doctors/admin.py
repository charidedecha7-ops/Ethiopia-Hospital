from django.contrib import admin
from .models import Doctor, Nurse

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'specialization', 'license_number', 'consultation_fee', 'is_available', 'has_image']
    list_filter = ['specialization', 'is_available']
    search_fields = ['user__first_name', 'user__last_name', 'license_number']
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Professional Details', {
            'fields': ('license_number', 'specialization', 'qualification', 'experience_years')
        }),
        ('Availability', {
            'fields': ('available_days', 'available_time_start', 'available_time_end', 'is_available')
        }),
        ('Consultation', {
            'fields': ('consultation_fee',)
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )
    
    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Has Image'

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ['user', 'department', 'shift', 'license_number']
    list_filter = ['department', 'shift']
    search_fields = ['user__first_name', 'user__last_name', 'license_number']
