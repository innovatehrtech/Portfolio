from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags
import threading

def _send_email_thread(subject, html_content, to_email):
    """
    Private function to actually send the email in a background thread.
    """
    try:
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=settings.EMAIL_HOST_USER,
            to=[to_email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def send_enquiry_confirmation_email(enquiry):
    """
    Sends a beautiful HTML confirmation email to the user asynchronously.
    """
    subject = f"Thank you for contacting Innovated HR Tech Compliance, {enquiry.name}!"

    html_content = render_to_string('Portfolio/emails/enquiry_confirmation.html', {
        'name': enquiry.name,
        'mobile': enquiry.contact_no,
        'email': enquiry.corporate_email,
        'company': enquiry.company_name,
        'designation': enquiry.designation,
        'enquiry_for': enquiry.enquiry_for,
        'message': enquiry.message,
    })
    
    email_thread = threading.Thread(
        target=_send_email_thread,
        args=(subject, html_content, enquiry.corporate_email)
    )

    email_thread.daemon = True
    email_thread.start()
