from django.urls import path
from . views import *

urlpatterns = [
    path('', ContactList.as_view()),
    path('?P<int:id>.+?', ContactDetailView.as_view()),
]