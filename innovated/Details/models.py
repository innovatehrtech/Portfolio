from django.db import models

from django.db import models

class ContactInquiry(models.Model):

    USER_TYPES = (
        ('Student', 'Student'),
        ('Employee', 'Employee'),
        ('Customer', 'Customer'),
    )

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    message = models.TextField()

    # Student-specific fields
    university = models.CharField(max_length=200, blank=True, null=True)
    course = models.CharField(max_length=200, blank=True, null=True)
    graduation_year = models.IntegerField(blank=True, null=True)

    # Employee-specific fields
    company = models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)

    # Customer-specific fields
    company_name = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    company_size = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    