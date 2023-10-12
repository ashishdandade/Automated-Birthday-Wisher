
from django.core.management.base import BaseCommand
from email_system.models import Employee, Event, EmailTemplate

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        employees = [
            {'name': 'ashish', 'email': 'ashishdandade6@gmail.com'},
            {'name': 'Rushikesh', 'email': 'ashishdandade326@gmail.com'},
        ]

        for employee_data in employees:
            Employee.objects.create(**employee_data)

        email_templates = {
            'Birthday': {
                'subject': 'Happy Birthday, {employee_name}!',
                'content': 'Dear {employee_name},\n\nWishing you a fantastic birthday!'
            },
            'Work Anniversary': {
                'subject': 'Congratulations on your Work Anniversary, {employee_name}!',
                'content': 'Dear {employee_name},\n\nCongratulations on your work anniversary!'
            },
        }

        for event_type, template_data in email_templates.items():
            EmailTemplate.objects.create(event_type=event_type, **template_data)

        events = [
            {'employee_name': 'ashish', 'event_type': 'Birthday', 'event_date': '2023-10-12'},
            {'employee_name': 'Rushikesh', 'event_type': 'Work Anniversary', 'event_date': '2023-10-12'},
        ]

        for event_data in events:
            employee = Employee.objects.get(name=event_data['employee_name'])
            event_type = event_data['event_type']
            event_date = event_data['event_date']
            Event.objects.create(employee=employee, event_type=event_type, event_date=event_date)

        self.stdout.write(self.style.SUCCESS('Sample data populated successfully'))
