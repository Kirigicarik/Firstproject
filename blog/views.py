from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
from .models import *
from .form import *


# Create your views here.


def blog_views(request):
    posts = Blog.objects.all()
    return render(request, 'Blog/index.html', {'post': posts})


def blog_detail(request, slug):
    post = get_object_or_404(Blog, Slug=slug)
    comments = post.comments.filter(Active=True, Parent__isnull=True)
    if request.method == 'Post':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            Parent_obj = None
            try:
                Parent_id = int(request.POST.get('Parent_id'))
            except:
                Parent_id = None
                if Parent_id:
                    Parent_obj = Comment.objects.get(id = Parent_id)
                    if Parent_obj:
                        reply_comment = comment-form.save(commit=False)
                        reply_comment.Parent = Parent_obj
                        new_comment = comment_form.save(commit=False)
                        new_comment.Post = post
                        new_comment.save()
                        return redirect('blog:detail', Slug)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/detail.html', {'blog': post, 'comment': comments, 'comment_form': comment_form})
