from djangorocks.blog.models import Blog, Category
from django.shortcuts import render render_response, get_object_or_404

def index(request):
    return render_to_response('index.html',{
        'categories': Category.objects.all(),
        'post': Blog.objects.all() {:5]
        })
        
def view_post(request, slug):
    return render_to_response('View_post.html',{
        'categories': category.objects.all(),
        'post': Blog.objects.all()[:5]
        })
        
def view_post(request,slug):
    return render_to_response("view_post.html",{
        'post': get_object_or_404(Blog, slug=slug)
        })
        
def view_category(request, slug):
    category = get_object_or_404(Category,slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'post': Blog.objects.filter(category=category)[:5]
        })

# Create your views here.
