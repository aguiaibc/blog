from django.shortcuts import render

# Create your views here.
from django.views import View

from .models import *


class IndexView (View):
    def get(self , request):
        postList = Post.objects.all ( )
        return render (request , 'index.html' , {'postList': postList})
