from django.views import generic

from ..models import Answer
from ..forms import AnswerForm

from questions_app.models import Question

class AnswersCreateView(generic.CreateView):
    model = Answer
    template_name = 'answers/answer_create.html'
    form_class = AnswerForm
    
    def form_valid(self, form):
        question_id = self.kwargs['pk']
        question = Question.objects.get(pk=question_id)
        form.instance.question = question
        return super().form_valid(form)
    
    def get_success_url(self):
        question_id = self.kwargs['pk']
        question = Question.objects.get(pk=question_id)
        return question.get_absolute_url()