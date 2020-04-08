from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #import nedded to require to the user be logged in and be the author to update or delete it
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #class based view
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] #show new posts up in page

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): #overwrite form validation method
        form.instance.author = self.request.user #set author as logged in user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): #overwrite form validation method
        form.instance.author = self.request.user #set author as logged in user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: #verify if the user is the same that posted the recipe
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: #verify if the user is the same that posted the recipe
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
