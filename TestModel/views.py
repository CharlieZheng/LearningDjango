
"""fuction docstring"""
from django.http import   HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question


class IndexView(generic.ListView):
    """View for index"""
    template_name = 'TestModel_Whatever/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    """View for detail"""
    model = Question
    template_name = 'TestModel_Whatever/detail.html'
class ResultsView(generic.DetailView):
    """View for results"""
    model = Question
    template_name = 'TestModel_Whatever/results.html'
def vote(request, question_id):
    """fuction docstring"""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'TestModel_Whatever/detail.html',
                      {'error_message': "You didn't select a choice.", 'question': question, })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('TestModelAppName:results', args=(question.id,)))
