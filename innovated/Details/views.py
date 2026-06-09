from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            inquiry = form.save()
            
            # Build email content based on user type
            user_email_content = f'''
Hello {inquiry.name},

Thank you for contacting Innovated HR Tech.

We received your enquiry successfully.
'''
            
            admin_email_content = f'''
New Inquiry Received

Name: {inquiry.name}
Email: {inquiry.email}
Phone: {inquiry.phone}
Type: {inquiry.user_type}
'''
            
            # Add type-specific details
            if inquiry.user_type == 'Student':
                user_email_content += f'''
University: {inquiry.university}
Course: {inquiry.course}
Graduation Year: {inquiry.graduation_year}
'''
                admin_email_content += f'''
University: {inquiry.university}
Course: {inquiry.course}
Graduation Year: {inquiry.graduation_year}
'''
            elif inquiry.user_type == 'Employee':
                user_email_content += f'''
Company: {inquiry.company}
Designation: {inquiry.designation}
Department: {inquiry.department}
'''
                admin_email_content += f'''
Company: {inquiry.company}
Designation: {inquiry.designation}
Department: {inquiry.department}
'''
            elif inquiry.user_type == 'Customer':
                user_email_content += f'''
Company Name: {inquiry.company_name}
Industry: {inquiry.industry}
Company Size: {inquiry.company_size}
'''
                admin_email_content += f'''
Company Name: {inquiry.company_name}
Industry: {inquiry.industry}
Company Size: {inquiry.company_size}
'''
            
            user_email_content += f'''
Message:
{inquiry.message}

Our team will contact you soon.

Regards,
Innovated HR Tech
'''
            
            admin_email_content += f'''
Message:
{inquiry.message}
'''
            
            # Mail to User
            send_mail(
                subject='Thank You for Contacting Innovated HR Tech',
                message=user_email_content,
                from_email='yourgmail@gmail.com',
                recipient_list=[inquiry.email],
                fail_silently=False
            )
            
            # Mail to Admin
            send_mail(
                subject=f'New Website Inquiry - {inquiry.user_type}',
                message=admin_email_content,
                from_email='innovatehrtech@gmail.com',
                recipient_list=['innovatehrtech@gmail.com'],
                fail_silently=False
            )
            
            messages.success(request, 'Your inquiry has been submitted successfully!')
            return redirect('details:contact_form')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})