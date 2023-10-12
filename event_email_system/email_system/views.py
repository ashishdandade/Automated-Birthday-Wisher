from email_system import views
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Employee, Event, EmailTemplate, EmailLog
import outlook

@csrf_exempt
@require_POST
def send_emails(request):
    current_date = date.today()
    events_today = Event.objects.filter(event_date=current_date)

    for event in events_today:
        employee = event.employee
        event_type = event.event_type
        email_template = EmailTemplate.objects.get(event_type=event_type)

        subject = email_template.subject.format(employee_name=employee.name)
        content = email_template.content.format(employee_name=employee.name)

        # Send the email using Outlook
        outlook.send_email(
            recipient=employee.email,
            subject=subject,
            body=content,
            sender='ashishdandade@outlook.com',
            password='Manisha@8390'
        )

        # Log the email status
        EmailLog.objects.create(
            employee=employee,
            event_type=event_type,
            event_date=current_date,
            email_sent=True
        )

    return JsonResponse({'message': 'Emails sent successfully'})
