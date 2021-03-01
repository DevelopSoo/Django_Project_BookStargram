from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
import pdb


def main(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'bookst/main.html', context)


@login_required(login_url='common:login')
def new(request):
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'bookst/new.html', context)


@require_POST
def create(request):
    form = PostForm(request.POST, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
    # pdb.set_trace()
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # # Post(title=title, content=content).save()
    # Post.objects.create(title=title, content=content)
    return redirect(form.instance)


def detail(request, post_id):
    # post_id = request.GET.get('post_id')
    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    default_view_count = post.view_count
    post.view_count = default_view_count + 1
    post.save()
    context = {
        'post': post
    }
    return render(request, 'bookst/detail.html', context)


@login_required(login_url='common:login')
def edit(request, post_id):
    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, "수정 권한이 없습니다.")
        return redirect('bookst:detail', post_id=post_id)
    context = {
        'post': post,
        'form': PostForm(instance=post)
    }
    return render(request, 'bookst/edit.html', context)



@require_POST
def update(request, post_id):
    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
    return redirect(post)


@require_POST
def delete(request, post_id):
    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('main')