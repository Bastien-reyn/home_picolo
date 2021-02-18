import json
import random

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from home_picolo.models import Question
from picolo.settings import BASE_DIR


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
    return HttpResponse(template.render({'list': json.dumps(p), 'color': 'darkslategray', 'players': request.COOKIES.get('players')}, request))


def drink(request):
    p = []
    template = loader.get_template('question.html')
    questions = Question.objects.filter(type=2)
    for q in questions:
        p.append({'question': q.question, 'type': q.type})
    return HttpResponse(template.render({'list': json.dumps(p), 'color': 'seagreen', 'players': request.COOKIES.get('players')}, request))


def hot(request):
    p = []
    template = loader.get_template('question.html')
    questions = Question.objects.filter(type=3)
    for q in questions:
        p.append({'question': q.question, 'type': q.type})
    return HttpResponse(template.render({'list': json.dumps(p), 'color': 'darkred', 'players': request.COOKIES.get('players')}, request))


def tod(request):
    p = []
    template = loader.get_template('question.html')
    questions = Question.objects.filter(type=4)
    for q in questions:
        p.append({'question': q.question, 'type': q.type})
    return HttpResponse(template.render({'list': json.dumps(p), 'color': '#0dcaf0', 'players': request.COOKIES.get('players')}, request))


def add(request):
    print(request.COOKIES.get('players'))
    print(request.POST.get('type'))
    questions = Question.objects.all().order_by('type')
    if request.POST.get('question') is not None and request.POST.get('type') is not None and request.POST.get('type') in ['1','2','3', '4']:
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
    if request.POST.get('question') is not None and request.POST.get('type') is not None and request.POST.get('type') in ['1','2','3', '4']:
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

'''
def csv(request):
   filename = str(BASE_DIR / 'default-2.json')
    f = open(filename, 'r')
    txt = f.read()
    dt = json.loads(txt)
    print(dt[0])
    for d in dt:
        if d.get('language') == 'fr' and d.get('nb_players') <= 2:
            if d.get('pack_name') == 'default':
                Question_of.objects.create(question=d.get('text'), type=1)
            elif d.get('pack_name') == 'hot':
                Question_of.objects.create(question=d.get('text'), type=3)
    qs = Question_of.objects.all()
    for q in qs:
        q.question = q.question.replace('%s', '%', 1).replace('%s', '%%')
        q.save()
    return JsonResponse([], safe=False)'''


