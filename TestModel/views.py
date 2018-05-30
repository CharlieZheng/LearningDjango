
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from .models import Choice, Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list, }
    return render(request, 'TestModel_Whatever/index.html', context)
    # template = loader.get_template('TestModel_Whatever/index.html')
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'TestModel_Whatever/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'TestModel_Whatever/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'TestModel_Whatever/detail.html', {'error_message': "You didn't select a choice.", 'question': question, })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('TestModelAppName:results', args=(question.id,)))
