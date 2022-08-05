from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('blogpage/', views.HomeBlogView, name='blogpage'),
    path('add_post/', views.UserAddPost, name='add_post'),
    path('<slug>/', views.blogPostDetail, name='blog_post_details'),
    path('edit_post/<slug:slug>/', views.BlogPostEdit, name='edit_post'),
    path('delete_post/<slug:slug>/', views.deletePost, name='delete_post'),
]
