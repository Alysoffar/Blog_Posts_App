from typing import Any
from django.db.models.query import QuerySet # type: ignore
from django.shortcuts import render ,get_object_or_404# type: ignore
from django.http import HttpResponse # type: ignore
from .models import Post
import boto3 # type: ignore
from django.conf import settings # type: ignore
from django.views.generic import ListView , DetailView , CreateView , UpdateView ,DeleteView # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin# type: ignore
from django.contrib.auth.models import User # type: ignore
# Create your views here.

def home(request):
    context ={
        'posts':Post.objects.all()
    }
    return render(request , 'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


    def get_queryset(self):
            queryset = super().get_queryset()
            for post in queryset:
                try:
                    print(post.author.profile.image.url)
                except Exception as e:
                    print(f"Error accessing image URL for post {post.id}: {e}")
            return queryset




class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html' 
    context_object_name = 'posts'
    paginate_by = 5
    def get_queryset(self) :
        user = get_object_or_404(User , username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDeatailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)    
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    return render(request , 'blog/about.html',{'title':'About'})
