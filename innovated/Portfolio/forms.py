from django import forms
# pyrefly: ignore [missing-import]
from .models import BusinessEnquiry

class BusinessEnquiryForm(forms.ModelForm):
    class Meta:
        model = BusinessEnquiry
        fields = ['name', 'corporate_email', 'company_name', 'designation', 'contact_no', 'location', 'enquiry_for', 'heard_about', 'message', 'terms_accepted']