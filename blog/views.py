from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest
from django.shortcuts import render

from .models import Post


def main(request):
    all_posts = Post.objects.filter(visible=True).order_by('date_published')
    paginator = Paginator(all_posts, 3)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'main.html', {
                  'title': 'Blog de JSM', 'posts': posts})


def post_detail(request, post_id):
    post = Post.objects.filter(pk=post_id)
    if not post:
        return HttpResponseBadRequest()

    post = post.first()
    return render(request, 'post_detail.html', {'post': post})
