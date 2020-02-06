#from django.shortcuts import render
from django.http import HttpResponse

from .models import Question , Choice
# Create your views here.

def printMessage(request) :
    return HttpResponse('This is a message')


def get_votes(request , question_id) :
    list = Question.objects.all()

    for i in list :
        if question_id == i.pk :
            return HttpResponse('Votes choice for Question ' + str(i) + ' with id ' +  str(question_id))

        else:
            return HttpResponse('Question id does not exists ')
