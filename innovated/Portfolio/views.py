from django.db.models import Q
# pyrefly: ignore [missing-import]
from .models import ComplianceLaw
from django.shortcuts import render, redirect
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
    return render(request, 'Portfolio/home.html')

def about(request):
    return render(request, 'Portfolio/about.html')

def services(request):
    return render(request, 'Portfolio/services.html')

def contact(request):
    return render(request, 'Portfolio/contact.html')

def compliance_risk_audit(request):
    return render(request, 'Portfolio/compliance_risk_audit.html')

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
