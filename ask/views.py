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

ANSWERS = {
    1: {'id': 1, 'like': 3, 'text': 'First of all I would like to thanks you for the invitation to participate in '
                                    'such a ... '
                                    'Russian is the huge territory which in many respects needs to be render '
                                    'habitable. '
                                    'First of all I would like to thanks you for the invitation to participate in '
                                    'such a ... '
                                    'Russian is the huge territory which in many respects needs to be render '
                                    'habitable.'},
    2: {'id': 2, 'like': 2, 'text': 'Russian is the huge territory which in many respects needs to be render '
                                    'habitable. '
                                    'First of all I would like to thanks you for the invitation to participate in '
                                    'such a ... '
                                    'Russian is the huge territory which in many respects needs to be render '
                                    'habitable. '
                                    'First of all I would like to thanks you for the invitation to participate in '
                                    'such a ...'},
    3: {'id': 3, 'like': 0, 'text': 'Yes, you`re absolute right! '
                                    'Yes, you`re absolute right! '
                                    'Yes, you`re absolute right! '
                                    'Yes, you`re absolute right! '
                                    'Yes, you`re absolute right!'},
}

QUESTIONS = {
    '1': {'id': 1, 'like': 9, 'answers': [ANSWERS[1], ANSWERS[2], ANSWERS[3]], 'title': 'How to build a moon park?',
          'q_tags': {TAGS[6], TAGS[8]},
          'text': 'Guys, I have trouble with a moon park. '
                  'Can`t find th black-jack... '
                  'Guys, I have trouble with a moon park. '
                  'Can`t find th black-jack...'},
    '2': {'id': 2, 'like': 7, 'answers': [ANSWERS[3]], 'title': 'I`m your eyes', 'q_tags': {TAGS[3], TAGS[4]},
          'text': 'I`m your eyes when you must steal'},
    '3': {'id': 3, 'like': 4, 'answers': [ANSWERS[2], ANSWERS[3]], 'title': 'I`m your pain',
          'q_tags': {TAGS[1], TAGS[2]},
          'text': 'I`m your pain when you can`t feel'},
}

USERS = {
    1: {'login': 'dr_pepper', 'name': 'Dr. Pepper', 'email': 'dr.pepper@mail.ru'}
}


def index(request):
    return render(request, 'index.html', {'singin': True, 'hot': False, 'questions': QUESTIONS.values(),
                                          'tags': TAGS.values()})


def hot(request):
    return render(request, 'index.html', {'singin': True, 'hot': True, 'questions': QUESTIONS.values(),
                                          'tags': TAGS.values()})


def questions_by_tag(request, tag_name):
    return render(request, 'tag.html', {'singin': False, 'tag_name': tag_name, 'questions': QUESTIONS.values(),
                                        'tags': TAGS.values()})


def question_detail(request, question_id):
    return render(request, 'question.html', {'singin': True, 'question': QUESTIONS.get(question_id),
                                             'tags': TAGS.values()})


def login(request):
    return render(request, 'login.html', {'singin': False, 'tags': TAGS.values()})


def singup(request):
    return render(request, 'signup.html', {'singin': False, 'tags': TAGS.values()})


def ask(request):
    return render(request, 'ask.html', {'singin': True, 'tags': TAGS.values()})


def settings(request):
    return render(request, 'settings.html', {'singin': True, 'user': USERS[1],
                                             'tags': TAGS.values()})
