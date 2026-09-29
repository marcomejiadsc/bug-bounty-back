from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Ticket
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    # Queryset: Defines the base data pool and default ordering (newest first)
    queryset = Ticket.objects.all().order_by('-created_at')
    
    # Serializer: Handles the translation between Model and JSON
    serializer_class = TicketSerializer
    
    # Permissions: Ensures only logged-in users can access these endpoints
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Intercept the creation process just before saving to the database.
        This injects the current authenticated user as the ticket reporter,
        preventing users from creating tickets on behalf of others.
        """
        serializer.save(reporter=self.request.user)