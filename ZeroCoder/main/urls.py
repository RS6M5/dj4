from django.urls import path
from . import views  # Corrected import statement

urlpatterns = [
    path('', views.new),  # Use views.index to refer to the view function
]
