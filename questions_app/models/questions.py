from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Question(models.Model):

    TITLE_CHOICES = (
        ('Технология', 'Технология'),
        ('Наука', 'Наука'),
        ('Исскусство и Литература', 'Исскусство и Литература'),
        ('Здоровье и Медицина', 'Здоровье и Медицина'),
        ('Бизнесс и Финанс', 'Бизнесс и Финанс'),
        ('Путешествие и Туризм', 'Путешествие и Туризм'),
        ('Образование', 'Education'),
        ('Спорт и Фитнес', 'Sports & Fitness'),
        ('Еда и Готовка', 'Food & Cooking'),
        ('Развлечение', 'Entertainment'),
        ('История', 'History'),
        ('Отношения и Знакомства', 'Relationships & Dating'),
        ('Политики и Правительство', 'Politics & Government'),
        ('Окружающая среда и Устойчивость', 'Environment & Sustainability'),
        ('Религия и Духовность', 'Religion & Spirituality'),
        ('Личностное развитие и Саморазвитие', 'Personal Development & Self-Improvement'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                             verbose_name="Пользователь")
    title = models.CharField("Описание", max_length=250)
    question_category = models.CharField(verbose_name="категория", max_length=250, 
                                         choices=TITLE_CHOICES)
    question_text = models.TextField("Текст вопроса")
    date_created = models.DateTimeField("Время добавления вопроса", auto_now_add=True)
    
    class Meta:
        ordering = ["question_text"]
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail_view', kwargs={'pk': self.pk})
