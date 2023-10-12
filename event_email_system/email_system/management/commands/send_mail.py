from django.core.management.base import BaseCommand
from email_system.models import Event, Employee, EmailTemplate
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Command(BaseCommand):
    help = 'Send event-related emails using Outlook'

    def handle(self, *args, **kwargs):
        from datetime import date
        current_date = date.today()

        events_today = Event.objects.filter(event_date=current_date)

        for event in events_today:
            employee = event.employee
            event_type = event.event_type

            email_template = EmailTemplate.objects.get(event_type=event_type)

            subject = email_template.subject.format(employee_name=employee.name)
            content = email_template.content.format(employee_name=employee.name)

            try:
                smtp_server = 'smtp-mail.outlook.com'
                smtp_port = 587
                sender_email = 'ashishdandade@outlook.com'
                sender_password = 'Manisha@8390'

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = employee.email
                msg['Subject'] = subject
                msg.attach(MIMEText(content, 'plain'))

                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, employee.email, msg.as_string())
                server.quit()

                self.stdout.write(self.style.SUCCESS(f'Successfully sent {event_type} email to {employee.name}'))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Failed to send {event_type} email to {employee.name}: {str(e)}'))
