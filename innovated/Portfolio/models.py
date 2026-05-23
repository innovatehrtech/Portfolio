from django.db import models

class BusinessEnquiry(models.Model):
    ENQUIRY_TYPES = [
        ('Compliance Risk Audit', 'Compliance Risk Audit'),
        ('Establishment Compliances', 'Establishment Compliances'),
        ('Payroll Compliance Services', 'Payroll Compliance Services'),
        ('Factory Compliance Services', 'Factory Compliance Services'),
        ('Other', 'Other')
    ]

    HEARD_ABOUT = [
        ('Google', 'Google Search'),
        ('LinkedIn', 'LinkedIn'),
        ('Referral', 'Referral'),
        ('Social Media', 'Social Media'),
        ('Event', 'Event/Conference'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    corporate_email = models.EmailField()
    company_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    enquiry_for = models.CharField(max_length=50, choices=ENQUIRY_TYPES)
    heard_about = models.CharField(max_length=50, choices=HEARD_ABOUT, blank=True)
    message = models.TextField(blank=True)
    terms_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.company_name}"
    class Meta:
        db_table = 'business_enquiry'

class ComplianceLaw(models.Model):
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=255)
    official_link = models.URLField(max_length=500)
    pdf_link = models.URLField(max_length=500)
    key_details = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'compliancelaw'
    

