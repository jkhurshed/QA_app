from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                             verbose_name="Пользователь")
    question_text = models.TextField("Текст вопроса")
    date_created = models.DateTimeField("Время добавления вопроса", auto_now_add=True)
    
    class Meta:
        ordering = ["question_text"]
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
    
    def __str__(self) -> str:
        return self.question_text
