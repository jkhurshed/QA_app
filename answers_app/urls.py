from django.urls import path
from .views import *

urlpatterns = [
    path('question/detail/<int:pk>/answer/create/', AnswersCreateView.as_view(), name='answer_create'),
    
]