from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                             verbose_name="Пользователь")
    question_text = models.ForeignKey("questions_app.Question", on_delete=models.CASCADE, 
                                      verbose_name="Текст вопроса")
    answer_text = models.TextField("Текст ответа")
    image_answer = models.ImageField("Фото ответ", upload_to="media/images/", blank=True)
    video_answer = models.URLField("Видео ответ", max_length=250, blank=True)
    audio_answer = models.FileField("Аудио", upload_to="media/audio/", blank=True)
    date_created = models.DateTimeField("Время добавления ответа", auto_now_add=True)

    class Meta:
        ordering = ["user"]
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
    
    def __str__(self) -> str:
        return self.answer_text
    