from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from blog.forms import BlogForm
from blog.models import Blog
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class BlogCreate(CreateView):
    template_name = 'blog/blog_form.html'
    form_class = BlogForm
    success_url = '/blog/list/'

@method_decorator(login_required, name='dispatch')
class BlogUpdate(UpdateView):
    model = Blog
    fields = ['title', 'description', 'tags']
    template_name = 'blog/blog_form.html'
    success_url = '/blog/list/'

@method_decorator(login_required, name='dispatch')
class BlogList(ListView):
    model = Blog
