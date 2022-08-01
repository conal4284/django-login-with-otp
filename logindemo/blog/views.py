from curses.ascii import CR
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from blog.forms import BlogForm
from blog.models import Blog

# Create your views here.
class BlogCreate(CreateView):
    template_name = 'blog/blog_form.html'
    form_class = BlogForm
    success_url = '/blog/list/'

class BlogUpdate(UpdateView):
    model = Blog
    fields = ['title', 'description', 'tags']
    template_name = 'blog/blog_form.html'
    success_url = '/blog/list/'

class BlogList(ListView):
    model = Blog
