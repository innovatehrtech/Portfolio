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

class HomePage(models.Model):
    hero_title = models.CharField(max_length=500)
    hero_subtitle = models.TextField()
    banner_image_url = models.URLField(max_length=500, blank=True)
    
    def __str__(self):
        return "Home Page Content"
    class Meta:
        db_table = 'homepage'

class DomainCard(models.Model):
    title = models.CharField(max_length=200)
    icon_class = models.CharField(max_length=100)
    link_url = models.CharField(max_length=500, blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'domaincard'
        ordering = ['order']

class AboutPage(models.Model):
    hero_title = models.CharField(max_length=200)
    hero_description = models.TextField()
    mission_text = models.TextField()
    vision_text = models.TextField()
    
    def __str__(self):
        return "About Page Content"
    class Meta:
        db_table = 'aboutpage'

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    icon_class = models.CharField(max_length=100, default='fa-solid fa-user')
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} - {self.role}"
    class Meta:
        db_table = 'teammember'
        ordering = ['order']

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'service'
        ordering = ['order']

class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, related_name='features', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.text
    class Meta:
        db_table = 'servicefeature'
        ordering = ['order']

class ServicePage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    hero_title = models.CharField(max_length=500)
    hero_description = models.TextField()
    cta_button_text = models.CharField(max_length=100, default='Request Audit')
    
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'servicepage'

class ServiceCard(models.Model):
    service_page = models.ForeignKey(ServicePage, related_name='cards', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    icon_class = models.CharField(max_length=100)
    content = models.TextField()
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.service_page.title} - {self.title}"
    class Meta:
        db_table = 'servicecard'
        ordering = ['order']

class ServiceCardList(models.Model):
    card = models.ForeignKey(ServiceCard, related_name='list_items', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.text
    class Meta:
        db_table = 'servicecardlist'
        ordering = ['order']
