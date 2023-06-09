from django.contrib import admin
from .models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ('id', 'user', 'question_text', 'answer_text', 
                    'image_answer', 'video_answer', 'audio_answer', "date_created")
    list_display_links = ("user",)
