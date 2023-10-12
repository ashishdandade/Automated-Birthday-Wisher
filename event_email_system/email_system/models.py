from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=255)
    event_date = models.DateField()

class EmailTemplate(models.Model):
    event_type = models.CharField(max_length=255, unique=True)
    subject = models.CharField(max_length=255)
    content = models.TextField()

class EmailLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=255)
    event_date = models.DateField()
    email_sent = models.BooleanField()
    error_message = models.TextField(blank=True, null=True)
