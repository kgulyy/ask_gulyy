from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the ask index.")


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
