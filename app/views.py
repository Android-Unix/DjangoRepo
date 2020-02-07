#from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from django.shortcuts import  render , get_object_or_404
from django.urls import reverse
from .models import Question , Choice
from .forms import Create_Form
from django.core.mail import send_mail

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('pk')
    return render(request, 'index.html' , {'latest_question_list' : latest_question_list})

def detail_id(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request , 'details.html' , {'question_list' : question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id) :
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'app/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponse("Votes are " + str(selected_choice.votes))



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = Create_Form(request.POST)
        if form.is_valid():
            return HttpResponse("Submit Sussessful!!")
    else:
        form = Create_Form()

    return render(request, 'name.html', {'form': form})
