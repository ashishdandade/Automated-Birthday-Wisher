from django.urls import path
from email_system import views

urlpatterns = [
    path('send_emails/', views.send_emails, name='send_emails'),
]
