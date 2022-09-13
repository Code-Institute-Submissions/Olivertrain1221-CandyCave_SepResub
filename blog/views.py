from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Posts
from .forms import BlogForm
from django.contrib import messages
# Create your views here.


def HomeBlogView(request):
    blog_posts = Posts.objects.all()
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'blog/blogpage.html', context)


def blogPostDetail(request, slug):
    '''
    View to return individual blog post
    '''
    post = get_object_or_404(Posts, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/blog_post_details.html', context)


@login_required
def UserAddPost(request):
    """
    A view to give users ability to add a post
    """
    form = BlogForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_post_blog_post = form.save(commit=False)
            new_post_blog_post.author = request.user
            new_post_blog_post.save()
            messages.success(request, 'Wicked your post is LIVE!')
            return redirect(reverse('blog:blogpage'))
        else:
            messages.error(request, 'failed to add post!')
    template = 'blog/add_post.html'
    return render(request, template, context)


@login_required
def BlogPostEdit(request, slug):
    '''
    View to display prefilled form to edit a blog post
    and to handle form processing
    '''
    post = get_object_or_404(Posts, slug=slug)
    form = BlogForm(instance=post)
    if request.user == post.author:
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES or None, instance=post)
            if form.is_valid():
                changed_form = form.save(commit=False)
                changed_form.author = request.user
                changed_form.save()
                messages.success(request, 'Successfully edited your blog post')
                return redirect('blog:blogpage')
            else:
                messages.error(request, 'Failed to update blog post, \
                    please double check the form.')
    else:
        messages.error(request, 'This is not your post')

    context = {
        'form': form,
        'post': post
    }

    return render(request, 'blog/add_post.html', context)


@login_required
def deletePost(request, slug):
    '''
    View to handle the deletion of a blog post
    '''
    post = get_object_or_404(Posts, slug=slug)

    if request.user == post.author:
        post.delete()
        messages.success(request, 'The post has been deleted.')
    return redirect('blog:blogpage')
