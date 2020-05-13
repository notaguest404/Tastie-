from django.urls import path
from .views import *
from blog import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/favourites/<str:username>', PostFavouriteListView.as_view(), name='favourites'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('post/<int:pk>/<str:opition>', UpdatePostVote.as_view(), name='requirement_post_vote'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
