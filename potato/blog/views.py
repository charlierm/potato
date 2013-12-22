from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View, TemplateView

class HomeView(TemplateView):
    #Todo: Obviously I need to replace this with a paginated class based view
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context