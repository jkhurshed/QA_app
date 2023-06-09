from django.contrib import admin
from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ("id", "user", "title", "question_text", "question_category", "date_created")
    list_display_links = ("title",)
