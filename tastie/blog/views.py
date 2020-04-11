from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #import nedded to require to the user be logged in and be the author to update or delete it
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView #class based view
from .models import Post
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    paginate_by = 8
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] #show new posts up in page

class UserPostListView(ListView):
    model = Post
    paginate_by = 8
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username =self.kwargs.get('username')) #prevent access to unable profiles
        return Post.objects.filter(author=user).order_by('-date_posted') #order posts by most recents

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'difficulty', 'duration', 'servings', 'image', 'ingredients', 'method', 'tags']

    def form_valid(self, form): #overwrite form validation method
        form.instance.author = self.request.user #set author as logged in user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'difficulty', 'duration', 'servings', 'image', 'ingredients', 'method', 'tags']

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

class SearchResultsView(ListView):
    model = Post
    paginate_by = 8
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__icontains=query) | Q(author__username__icontains=query)
        )
        return object_list.order_by('-date_posted')
