from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
    return HttpResponse('Youz at index')