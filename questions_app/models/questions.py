from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Question(models.Model):

    TITLE_CHOICES = (
        ('technology', 'Technology'),
        ('science', 'Science'),
        ('arts & literature', 'Arts & Literature'),
        ('health & medicine', 'Health & Medicine'),
        ('business & finance', 'Business & Finance'),
        ('travel & tourism', 'Travel & Tourism'),
        ('education', 'Education'),
        ('sports & fitness', 'Sports & Fitness'),
        ('food & cooking', 'Food & Cooking'),
        ('entertainment', 'Entertainment'),
        ('history', 'History'),
        ('relationships & dating', 'Relationships & Dating'),
        ('politics & government', 'Politics & Government'),
        ('environment & sustainability', 'Environment & Sustainability'),
        ('religion & spirituality', 'Religion & Spirituality'),
        ('personal development & self-improvement', 'Personal Development & Self-Improvement'),
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
