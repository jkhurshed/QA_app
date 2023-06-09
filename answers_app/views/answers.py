from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from ..models import Answer
from ..forms import AnswerForm

from questions_app.models import Question

class AnswersCreateView(generic.CreateView):
    model = Answer
    template_name = 'answers/answer_create.html'
    form_class = AnswerForm
    
    def form_valid(self, form):
        question_id = self.kwargs['pk']
        question = get_object_or_404(Question, pk=question_id)
        form.instance.question = question
        form.instance.question_text_id = question_id
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        question_id = self.kwargs['pk']
        return reverse('detail_view', kwargs={'pk': question_id})
