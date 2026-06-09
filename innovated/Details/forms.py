from django import forms
from .models import ContactInquiry

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactInquiry
        fields = '__all__'
        widgets = {
            'user_type': forms.Select(attrs={'class': 'form-control', 'id': 'user_type'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message', 'rows': 4}),
            'university': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter university name'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course or degree'}),
            'graduation_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter graduation year', 'min': '2024', 'max': '2030'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter designation'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter department'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name'}),
            'industry': forms.Select(attrs={'class': 'form-control'}),
            'company_size': forms.Select(attrs={'class': 'form-control'}),
        }