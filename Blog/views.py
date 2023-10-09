from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Article

# Create your views here.

class Articles(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog/blog.html"

class CreateArticle(CreateView):
    model = Article
    template_name = "blog/createArticle.html"
    success_url = reverse_lazy('blog')
    fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'fecha_creacion', 'imagen']

class ReadArticle(DetailView):
    model         = Article
    template_name = "blog/detailArticle.html"
    
class EditArticle(UpdateView):
    model         = Article
    template_name = "blog/editArticle.html"
    success_url = reverse_lazy('blog')
    fields        = ['titulo', 'subtitulo', 'contenido', 'imagen']