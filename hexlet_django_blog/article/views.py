from django.shortcuts import render


def index(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'article/index.html',
        context={'tags': tags},
    )
