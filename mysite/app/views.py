#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import  render , get_object_or_404
from .models import Question , Choice
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-publication')
    return render(request, 'index.html' , {'latest_question_list' : latest_question_list})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request , 'details.html' , {'question_list' : question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
