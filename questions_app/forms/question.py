from django import forms
from ..models import Question


class QuestionForm(forms.ModelForm):
    title = forms.CharField(label='Question Title')
    
    class Meta:
        model = Question
        fields = ['user', 'title', 'question_category', 'question_text']
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 4}),
        }