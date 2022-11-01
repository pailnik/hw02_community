from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(requests):
    # text = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(requests, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def groups_list(request):
    template = 'posts/group_list.html'
    return render(request, template)