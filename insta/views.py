from distutils.log import error
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .models import Post

from insta.models import Contact

# Create your views here.
def index(request):
    allpost=Post.objects.all()
    content={'allpost':allpost}
    return render(request,"index.html",content)


def about(request):
    return render(request,"about.html",)

def blog(request):
    allpost=Post.objects.all()
    content={'allpost':allpost}
    return render(request,"blog.html",content)

def contact(request):
    messages.success(request, 'Contact us')
    if request.method=="POST":
        name=request.POST['firstname']
        last=request.POST['lastname']
        em=request.POST['email']
        mes=request.POST['message']    
        contact=Contact(fname=name,lname=last,email=em,message=mes)
        contact.save()
        
    return render(request,"contact.html",)

def post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'post.html', context)   


def undr(request):
    return render(request,'under.html',) 