from django.shortcuts import render
from .models import Blog, Comment, SendMessage
from .forms import CommentForm, SendMessageForm

# Create your views here.


def index(request):
    form = SendMessageForm()
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            message = SendMessage(
                name = form.cleaned_data["name"],
                email = form.cleaned_data["email"],
                message = form.cleaned_data["message"],

        )
        message.save()
    context = {
        "form": form,
    }

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    
    form = SendMessageForm()
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            message = SendMessage(
                name = form.cleaned_data["name"],
                email = form.cleaned_data["email"],
                message = form.cleaned_data["message"],

        )
        message.save()
    context = {
        "form": form,
    }

    return render(request, 'contact.html', context)

def blog(request):
    blogs = Blog.objects.all().order_by('-created')
    
    form = SendMessageForm()
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            message = SendMessage(
                name = form.cleaned_data["name"],
                email = form.cleaned_data["email"],
                message = form.cleaned_data["message"],

        )
        message.save()

    
    context ={
        'blogs' : blogs,
        "form": form,
    }
    return render(request, 'blog.html', context)


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                blog=blog
            )
            comment.save()

    comments = Comment.objects.filter(blog=blog)
    context = {
        "blog": blog,
        "comments": comments,
        "form": form,
    }
    return render(request, "detail.html", context)


def contact(request):
    
    form = SendMessageForm()
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            message = SendMessage(
                name = form.cleaned_data["name"],
                email = form.cleaned_data["email"],
                message = form.cleaned_data["message"],

        )
        message.save()
    context = {
        "form": form,
    }

    return render(request, 'contact.html', context)



def home(request):
    return render(request, 'home.html')