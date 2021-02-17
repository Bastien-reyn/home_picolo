import json
import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from home_picolo.models import Question


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def game(request):
    template = loader.get_template('game.html')
    return HttpResponse(template.render({}, request))


def normal(request):
    p = []
    template = loader.get_template('question.html')
    questions = Question.objects.filter(type=1)
    for q in questions:
        p.append({'question': q.question, 'type': q.type})
    return HttpResponse(template.render({'list': json.dumps(p), 'color': 'darkslategray'}, request))


def drink(request):
    p = []
    template = loader.get_template('question.html')
    questions = Question.objects.filter(type=2)
    for q in questions:
        p.append({'question': q.question, 'type': q.type})
    return HttpResponse(template.render({'list': json.dumps(p), 'color': 'seagreen'}, request))


def hot(request):
    p = []
    template = loader.get_template('question.html')
    questions = Question.objects.filter(type=3)
    for q in questions:
        p.append({'question': q.question, 'type': q.type})
    return HttpResponse(template.render({'list': json.dumps(p), 'color': 'darkred'}, request))


def add(request):
    print(request.COOKIES.get('players'))
    print(request.POST.get('type'))
    questions = Question.objects.all().order_by('type')
    if request.POST.get('question') is not None and request.POST.get('type') is not None and request.POST.get('type') in ['1','2','3']:
        try:
            Question.objects.create(type=request.POST.get('type'), question=request.POST.get('question'))
            return render(request, 'add.html', {
                'success_message': "Ajouté",
                'questions': questions
            })
        except:
            return render(request, 'add.html', {
                'error_message': "Erreur d'ajout",
                'questions': questions
            })
    return render(request, 'add.html', {'questions': questions})

@csrf_exempt
def add_api(request):
    if request.POST.get('question') is not None and request.POST.get('type') is not None and request.POST.get('type') in ['1','2','3']:
        try:
            q = Question.objects.get(id=request.POST.get('id'))
            q.type = request.POST.get('type')
            q.question = question = request.POST.get('question')
            q.save()
            return JsonResponse({
                'msg': "Ajouté",
                'success': True
            }, safe=False)
        except:
            return JsonResponse({
                'msg': "Echec",
                'success': False
            }, safe=False)
    return JsonResponse({
                'msg': "Echec",
                'success': False
            }, safe=False)





