from django.contrib import admin
from .models import LoanApplication

@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ('application_id', 'loan_amount', 'loan_term', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'education', 'self_employed')
    search_fields = ('application_id',)
    readonly_fields = ('application_id', 'created_at', 'is_approved')