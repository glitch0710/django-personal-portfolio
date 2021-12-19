from django.shortcuts import render, get_object_or_404
from blog.models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-post_date')[:5]
    count = Blog.objects.count()

    if count > 1:
        count = str(count) + ' blogs'
    else:
        count = str(count) + ' blog'

    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'count': count})


def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': blog})
