from django.shortcuts import render,get_object_or_404
from blog.models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name__iexact = kwargs['cat_name'])
    
    if kwargs.get('author_username')!= None:
        # when we want to point out to a field in another table that it relates to my element, 
        posts = posts.filter(author__username__iexact = kwargs['author_username'])
       
    if kwargs.get('tag_name') != None:
            posts = posts.filter(tags__name__in = [kwargs['tag_name']])
            pass
    
    # Paginator
    posts =  Paginator(posts, 3)
    page_num = request.GET.get('page')
    
    try:
        posts = posts.page(page_num)
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.page(1)
 
    context = {'posts':posts}
    
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts , pk=pid)
    comments = Comment.objects.filter(post=post.id, approved=True)
    context = {'post':post, 'comments':comments}
    
    return render(request, 'blog/blog-single.html', context)

''' def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    
    # __iexact is case-insensitive,
    # so it doesn't distinguish between uppercase and lowercase letters.
    posts = posts.filter(category__name__iexact=cat_name)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context) '''

def blog_search(request):
    posts = Post.objects.filter(status=1)
    
    # with __dict__ we can we the elements & attributes of the request obj
    # print(request.__dict__)
    
    if request.method == 'GET':
        #print(request.GET.get('s'))
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)
            
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)