from django.urls import reverse_lazy
from django.views import generic

from ..models import Question
from ..forms import QuestionForm

class QuestionListViewSet(generic.ListView):
    model = Question
    quetion_list = Question.objects.all()
    template_name = 'questions/question.html'


class QuestionDetailViewSet(generic.DetailView):
    model = Question
    context = Question.objects.all()
    template_name = 'questions/question_detail.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()
        context['question'] = question
        return context

