from django.urls import path,include
# pyrefly: ignore [missing-import]
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('submit-enquiry/', views.submit_enquiry, name='submit_enquiry'),
    path('compliance-risk-audit/', views.compliance_risk_audit, name='compliance_risk_audit'),
    path('establishment-compliances/', views.establishment_compliances, name='establishment_compliances'),
    path('payroll-compliance-services/', views.payroll_compliance_services, name='payroll_compliance_services'),
    path('factory-compliance-services/', views.factory_compliance_services, name='factory_compliance_services'),
    path('search/', views.search_laws, name='search_laws'),
    path('products/', views.products, name='products'),
    path('resources/', views.resources, name='resources'),
    path('recruiter/', include('Recruiter.urls')),
]
