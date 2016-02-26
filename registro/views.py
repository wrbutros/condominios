from django.shortcuts import render


def dashboard(request):
    context = {'latest_question_list': 'jojojo'}
    return render(request, 'registro/dashboard.html', context)


def index(request):
    context = {'latest_question_list': 'jojojo'}
    return render(request, 'registro/index.html', context)
