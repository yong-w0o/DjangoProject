from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog,Comment,CustomUser
from .forms import BlogForm,CommentForm
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('-pub_date')
    query = request.GET.get('query')
    if query:
        blogs = Blog.objects.filter(title__contains=query)
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    paginated_blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs' : paginated_blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog' : blog})

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form': form})

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        if request.user.is_authenticated:
            new_blog.user = request.user
        new_blog.save()
        return redirect('blog:detail', new_blog.id)
    return redirect('home')

def update(request, id):
    blog = Blog.objects.get(id = id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()
        return redirect('blog:detail', blog.id)
    return render(request, 'update.html', {'blog' : blog})

def delete(request, id):
    blog = Blog.objects.get(id = id)
    blog.delete()
    return redirect('home')

def newreply(request):
    if request.method == "POST":
        comment = Comment()
        comment.comment_body = request.POST['comment_body']
        comment.blog = Blog.objects.get(pk=request.POST['blog'])
        author = request.POST['user']
        print(type(author), author)
        if author:
            comment.comment_user = CustomUser.objects.get(username=author)
        else:
            return redirect('blog:detail', comment.blog.id)
        comment.comment_date = timezone.now()
        comment.save()

        return redirect('blog:detail', comment.blog.id)
    else:
        return redirect('home')

def replydelete(request, id):
    comment = get_object_or_404(Comment, pk=id)
    blog_id = comment.blog.id
    comment.delete()
    return redirect('blog:detail', blog_id)