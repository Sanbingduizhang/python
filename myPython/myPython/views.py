from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    content = {}
    content['hello'] = "hello world!"
    return render(request, 'hello.html', content)
    # return HttpResponse("hello World ! ")
