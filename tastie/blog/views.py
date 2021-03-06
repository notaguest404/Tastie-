from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #import nedded to require to the user be logged in and be the author to update or delete it
from django.views.generic import RedirectView,TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View #class based view
from blog.models import Post, DisLike, Like
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse
from .forms import CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['likes'] #show new posts up in page

class PostFavouriteListView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/favourite.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username =self.kwargs.get('username')) #prevent access to unable profiles
        return Post.objects.order_by('title') #order posts by most recents

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
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'difficulty', 'duration', 'servings', 'image', 'ingredients', 'method', 'tags']

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
            Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__slug__icontains=query) | Q(author__username__icontains=query)
        )
        return object_list.order_by('-date_posted')

class UpdatePostVote(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):

        pk = self.kwargs.get('pk', None)
        opition = self.kwargs.get('opition', None) # like or dislike button clicked

        post = get_object_or_404(Post, id=pk)

        try:
            # If child DisLike model doesnot exit then create
            post.dis_likes
        except Post.dis_likes.RelatedObjectDoesNotExist as identifier:
            DisLike.objects.create(post = post)

        try:
            # If child Like model doesnot exit then create
            post.likes
        except Post.likes.RelatedObjectDoesNotExist as identifier:
            Like.objects.create(post = post)

        if opition.lower() == 'like':

            if request.user in post.likes.users.all():
                post.likes.users.remove(request.user)
            else:
                post.likes.users.add(request.user)
                post.dis_likes.users.remove(request.user)

        elif opition.lower() == 'dis_like':

            if request.user in post.dis_likes.users.all():
                post.dis_likes.users.remove(request.user)
            else:
                post.dis_likes.users.add(request.user)
                post.likes.users.remove(request.user)
        else:
            return redirect('post-detail', pk=pk)
        return redirect('post-detail', pk=pk)

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            form.instance.author = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post-detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post-detail', pk=comment.post.pk)
