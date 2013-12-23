from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.views.generic import ListView, DetailView
from blog.models import Post

class IndexView(ListView):

    template_name = "blog/index.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(draft=False)



class DetailView(DetailView):
#Todo: Obviously I need to replace this with a paginated class based view
    template_name = "blog/detail.html"
    model = Post