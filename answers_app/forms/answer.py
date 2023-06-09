from django import forms
from ..models import Answer
from questions_app.models import Question

class AnswerForm(forms.ModelForm):

    class Meta:

        model = Answer
        # fields = ['answer_text', 'image_answer', 'video_answer']
        fields = ['answer_text']
        widgets = {
            # 'user': forms.Select(attrs={'class': 'form-control'}),
            # 'question_text': forms.Select(attrs={'class': 'form-control'}),
            'answer_text': forms.Textarea(attrs={'class': 'form-control my-custom-class', 'rows': 4}),
            # 'image_answer': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            # 'video_answer': forms.URLInput(attrs={'class': 'form-control'}),
            # 'audio_answer': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
