import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from home_picolo.models import Question


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def game(request):
    template = loader.get_template('game.html')
    return HttpResponse(template.render({}, request))


def normal(request):
    questions = Question.objects.filter(type=1)
    template = loader.get_template('question.html')
    return HttpResponse(template.render({'question': random.choice(questions), 'color': 'darkslategray'}, request))


def drink(request):
    questions = Question.objects.filter(type=2)
    template = loader.get_template('question.html')
    return HttpResponse(template.render({'question': random.choice(questions), 'color': 'seagreen'}, request))


def hot(request):
    questions = Question.objects.filter(type=3)
    template = loader.get_template('question.html')
    return HttpResponse(template.render({'question': random.choice(questions), 'color': 'darkred'}, request))


def add(request):
    questions = Question.objects.filter(type=3)
    template = loader.get_template('question.html')
    return HttpResponse(template.render({'question': random.choice(questions), 'color': 'darkred'}, request))


def add_api(request):
    questions = Question.objects.filter(type=3)
    template = loader.get_template('question.html')
    return HttpResponse(template.render({'question': random.choice(questions), 'color': 'darkred'}, request))




