from django.shortcuts import render
from blog.models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-post_date')
    count = Blog.objects.count()

    if count > 1:
        count = str(count) + ' blogs'
    else:
        count = str(count) + ' blog'

    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'count': count})
