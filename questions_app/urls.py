from django.urls import path, include
from .views import *

urlpatterns = [
    path('', QuestionListViewSet.as_view(), name="list_question"),
    path('question/detail/<int:pk>', QuestionDetailViewSet.as_view(), name="detail_view"),
]