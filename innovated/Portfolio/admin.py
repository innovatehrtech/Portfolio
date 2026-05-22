from django.contrib import admin
# pyrefly: ignore [missing-import]
from .models import BusinessEnquiry, ComplianceLaw

@admin.register(BusinessEnquiry)
class BusinessEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'corporate_email', 'company_name', 'enquiry_for', 'created_at')
    list_filter = ('enquiry_for', 'created_at')
    search_fields = ('name', 'corporate_email', 'company_name', 'location')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

@admin.register(ComplianceLaw)
class ComplianceLawAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'official_link')
    list_filter = ('category',)
    search_fields = ('name', 'category', 'key_details')
    ordering = ('category', 'name')

