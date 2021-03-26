from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import Note, Patient, User


class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Extra Fields', {'fields': ('patients',)}),
    )
    filter_horizontal = ('patients',)


class NoteAdmin(admin.ModelAdmin):
    fields = ('patient', 'nutritionist', 'description', 'date')
    raw_id_fields = ('patient', 'nutritionist')
    readonly_fields = ('date',)


class PatientAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email')


admin.site.register(Note, NoteAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(User, UserAdmin)
