from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, FormView, CreateView
from blog.models import Post
from django.contrib import messages

class IndexView(ListView):

    template_name = "blog/index.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(draft=False)

class DetailView(DetailView):
#Todo: Obviously I need to replace this with a paginated class based view
    template_name = "blog/detail.html"
    model = Post

class LoginView(TemplateView):
    template_name = "blog/login.html"

    def post(self, request, *args, **kwargs):
        user = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=user, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            messages.error(self.request, "Incorrect username or password")
            return render_to_response(self.template_name)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['messages'] = messages
        return context


class AdminPostListView(ListView):

    template_name = "blog/admin.html"
    model = Post


class AdminPostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'draft']
    template_name = 'blog/post_create.html'
