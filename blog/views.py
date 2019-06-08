from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Post


def main(request):
    all_posts = Post.objects.filter(visible=True).order_by('date_published')
    paginator = Paginator(all_posts, 5)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'main.html', {
                  'title': 'Blog de JSM', 'posts': posts})
