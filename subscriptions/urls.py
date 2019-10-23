from django.urls import path
from subscriptions.views import *

urlpatterns = [
    path('subscription', SubCreateView.as_view()),
]
