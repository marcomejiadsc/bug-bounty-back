from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet

# 1. Create a router and register our viewsets with it
router = DefaultRouter()

# 2. Automatically generate the URL routing for the TicketViewSet
router.register(r'tickets', TicketViewSet, basename='ticket')

# 3. Wire up our API using automatic URL routing
urlpatterns = [
    path('', include(router.urls)),
]