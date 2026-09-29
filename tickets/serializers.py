from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    # Personalized field to show the creator user email instead numeric id only
    reporter_email = serializers.ReadOnlyField(source='reporter.email')

    class Meta:
        model = Ticket
        # Fields defined to expose to the frontend
        fields = [
            'id', 
            'title', 
            'description', 
            'severity', 
            'status', 
            'reporter', 
            'reporter_email', 
            'created_at', 
            'updated_at'
        ]
        # Reporter is defined as read-only because it will be assigned automatically in the view
        
        read_only_fields = ['reporter', 'created_at', 'updated_at']