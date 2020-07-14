from django.shortcuts import render

from django.http import HttpResponse

from .models import Question

from django.shortcuts import render, get_object_or_404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/index.html', context)
    # TODO add pagination 

# def detail(request, question_id):
#     return HttpResponse(f"You are looking at Question {question_id}")
    


def results(request, question_id):
    return HttpResponse(f"You are looking at RESULTS of Question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You are voting at Question {question_id}")
