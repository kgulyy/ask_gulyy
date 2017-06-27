from django.http import HttpResponse
from django.shortcuts import render

TAGS = {
    1: 'perl',
    2: 'python',
    3: 'TechnoPark',
    4: 'MySQL',
    5: 'django',
    6: 'Mail.Ru',
    7: 'Google',
    8: 'Firefox',
}

QUESTIONS = {
    '1': {'id': 1, 'like': 9, 'answer': 3, 'title': 'How to build a moon park?', 'q_tags': {TAGS[6], TAGS[8]},
          'text': 'Guys, I have trouble with a moon park. '
                  'Can`t find th black-jack... '
                  'Guys, I have trouble with a moon park. '
                  'Can`t find th black-jack...'},
    '2': {'id': 2, 'like': 7, 'answer': 4, 'q_tags': {TAGS[3], TAGS[4]}, 'title': 'I`m your eyes',
          'text': 'I`m your eyes when you must steal'},
    '3': {'id': 3, 'like': 4, 'answer': 1, 'title': 'I`m your pain', 'q_tags': {TAGS[1], TAGS[2]},
          'text': 'I`m your pain when you can`t feel'},
}


def index(request):
    return render(request, 'index.html', {'singin': True, 'questions': QUESTIONS.values(),
                  'tags': TAGS.values()})


def hot(request):
    return HttpResponse("Hello, world. You're at the hot url.")


def questions_by_tag(request, tag_name):
    return HttpResponse("You see questions by {0} tag".format(tag_name))


def question_detail(request, question_id):
    return HttpResponse("It's {0} question".format(question_id))


def login(request):
    return HttpResponse("Hello, world. You're at the login url.")


def singup(request):
    return HttpResponse("Hello, world. You're at the singup url.")


def ask(request):
    return HttpResponse("Hello, world. You're at the ask url.")


def settings(request):
    return HttpResponse("Hello, world. You're at the settings url.")
