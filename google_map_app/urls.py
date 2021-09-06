from django.urls import path, include
from .views import google_map_marker

urlpatterns = [
	path('google-map-marker/', google_map_marker.as_view(), name="dashboard"),
    ]