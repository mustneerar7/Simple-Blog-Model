from django.urls import path
from django.urls.resolvers import URLPattern
from .views import SignUpView

urlpatterns = [
    path('Signup/', SignUpView.as_view(), name = 'signup'),
    
]