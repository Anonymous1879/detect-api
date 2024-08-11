from django.urls import path
from .views import GPTDetectorView

urlpatterns = [
    path('detect/', GPTDetectorView.as_view(), name='gpt-detect'),  # Path for the POST request
]
