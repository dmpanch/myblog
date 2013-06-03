from blog.models import Post, Category
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5]
    })

def view_post(request, url_name):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Post, readeble_url=url_name)
    })

def view_category(request, url_name):
    category = get_object_or_404(Category, readeble_url=url_name)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5]
    })