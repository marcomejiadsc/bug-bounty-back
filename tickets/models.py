from django.db import models
from django.contrib.auth import get_user_model

# Get the user model
User = get_user_model()

class Ticket(models.Model): 
    # Prerefed choices for bug severity
    SEVERITY_CHOICES = [
        ('LOW', 'Baja'),
        ('MEDIUM', 'Media'),
        ('HIGH', 'Alta'),
        ('CRITICAL', 'Crítica'),
    ]

    # Choices for the ticket status
    STATUS_CHOICES = [
        ('OPEN', 'Abierto'),
        ('IN_PROGRESS', 'En Progreso'),
        ('RESOLVED', 'Resuelto'),
        ('CLOSED', 'Cerrado'),
    ]

    title = models.CharField(max_length=255, verbose_name="Título del Reporte")
    description = models.TextField(verbose_name="Descripción detallada y pasos para reproducir")
    
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='LOW')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='OPEN')
    
    # Relation: A user can report many tickets (ForeignKey)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_tickets')
    
    # Automatic dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.severity}] {self.title} - {self.status}"
