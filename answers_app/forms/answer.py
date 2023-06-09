from django import forms
from ..models import Answer

class AnswerForm(forms.ModelForm):
            
    class Meta:
        model = Answer
        fields = ['user', 'question_text', 'answer_text', 'image_answer', 
                  'video_answer', 'audio_answer']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'question_text': forms.Select(attrs={'class': 'form-control'}),
            'answer_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image_answer': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video_answer': forms.URLInput(attrs={'class': 'form-control'}),
            'audio_answer': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
