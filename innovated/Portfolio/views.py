from django.db.models import Q
# pyrefly: ignore [missing-import]
from .models import ComplianceLaw, HomePage, DomainCard, AboutPage, TeamMember, Service, ServicePage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# pyrefly: ignore [missing-import]
from .forms import BusinessEnquiryForm
# pyrefly: ignore [missing-import]
from .email import send_enquiry_confirmation_email

def submit_enquiry(request):
    if request.method == 'POST':
        form = BusinessEnquiryForm(request.POST)

        if form.is_valid():
            enquiry = form.save()
            send_enquiry_confirmation_email(enquiry)
            messages.success(
                request,
                "Thank you! Your enquiry has been submitted successfully."
            )
        else:
            messages.error(
                request,
                "There was an error submitting your enquiry. Please try again."
            )

    return redirect(request.META.get('HTTP_REFERER', 'home'))

def home(request):
    try:
        home_page = HomePage.objects.first()
    except HomePage.DoesNotExist:
        home_page = None
    
    domain_cards = DomainCard.objects.all()
    
    context = {
        'home_page': home_page,
        'domain_cards': domain_cards,
    }
    return render(request, 'Portfolio/home.html', context)

def about(request):
    try:
        about_page = AboutPage.objects.first()
    except AboutPage.DoesNotExist:
        about_page = None
    
    team_members = TeamMember.objects.all()
    
    context = {
        'about_page': about_page,
        'team_members': team_members,
    }
    return render(request, 'Portfolio/about.html', context)

def services(request):
    services_list = Service.objects.prefetch_related('features').all()
    
    context = {
        'services': services_list,
    }
    return render(request, 'Portfolio/services.html', context)

def contact(request):
    return render(request, 'Portfolio/contact.html')

def compliance_risk_audit(request):
    service_page = get_object_or_404(ServicePage, slug='compliance-risk-audit')
    
    context = {
        'service_page': service_page,
    }
    return render(request, 'Portfolio/compliance_risk_audit.html', context)

def establishment_compliances(request):
    return render(request, 'Portfolio/establishment_compliances.html')

def payroll_compliance_services(request):
    return render(request, 'Portfolio/payroll_compliance_services.html')

def factory_compliance_services(request):
    return render(request, 'Portfolio/factory_compliance_services.html')

def search_laws(request):
    query = request.GET.get('q', '').strip()
    if query:
        results = ComplianceLaw.objects.filter(
            Q(name__icontains=query) |
            Q(category__icontains=query) |
            Q(key_details__icontains=query)
        )
    else:
        results = ComplianceLaw.objects.all()
    
    results = results.order_by('category', 'name')

    categories_dict = {}
    for result in results:
        categories_dict.setdefault(result.category, []).append(result)
        
    context = {
        'query': query,
        'categories_dict': categories_dict,
        'results_count': results.count(),
        'all_laws_count': ComplianceLaw.objects.count()
    }
    return render(request, 'Portfolio/search_results.html', context)

def products(request):
    return render(request, 'Portfolio/products.html')

def resources(request):
    return render(request, 'Portfolio/resources.html')


