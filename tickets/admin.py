from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    # Columns that we want to see on the resume table
    list_display = ('title', 'severity', 'status', 'reporter', 'created_at')
    
    # Filter fields 
    list_filter = ('severity', 'status', 'created_at')
    
    # Searchable fields for the search bar
    search_fields = ('title', 'description', 'reporter__email')