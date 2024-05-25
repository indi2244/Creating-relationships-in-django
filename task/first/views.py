from django.shortcuts import render

from django.http import HttpResponse



def request(response):
    return HttpResponse('<h1> HIIII </h1>')


