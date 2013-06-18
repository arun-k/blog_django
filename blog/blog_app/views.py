# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from datetime import datetime
from models import Blog,Comment

#home page
def home(request):
    if request.method=='GET':
        return render_to_response('home.html')
    if request.method=='POST':
        usrname=request.POST['usrname']
        passwrd=request.POST['passwrd']
        user=authenticate(username=usrname,password=passwrd)
        if user is not None and user.is_active:
            login(request,user)
            return HttpResponse('/user/%s'%usrname)
        else:
            return HttpResponse("Invalid user!!!")

#register user
def register(request):
    if request.method=='GET':
        return render_to_response('register.html')
    if request.method=='POST':
        new_usrname=request.POST['usrname']
        new_email=request.POST['email']
        new_passwrd=request.POST['passwrd']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        user=User.objects.create_user(username=new_usrname,email=new_email,password=new_passwrd)
        user.first_name=firstname
        user.last_name=lastname
        user.save()
        return HttpResponse('/')

#user
def user_home(request,usrname):
    if request.method=='GET':
        usr=Blog.objects.filter(username=usrname)
        #usr_blog={}
        #for each in usr:
        #    usr_blog[each.topic]=each.content
        return render_to_response('userhome.html',{'usr':usr,'username':usrname})

#edit
def post_edit(request,blog_id):
    blog_id=int(blog_id)
    if request.method=='GET':
        blog=Blog.objects.get(id=blog_id)
        #blog_dic={}
        #blog_dic[blog.topic]=blog.content
        return render_to_response('postedit.html',{'post':blog})
    if request.method=='POST':
        topic=request.POST['topic']
        content=request.POST['content']
        blog=Blog.objects.get(id=blog_id)
	date_str=request.POST['date']
	d=datetime.strptime(date_str,'%Y-%m-%d')
	date=d.date()
        blog.topic=topic
        blog.content=content
	blog.created=date
        blog.save();
        return HttpResponse('/user/%s/'%blog.username)

#new post
def new_post(request,usrname):
    if request.method=='GET':
        return render_to_response('newpost.html',{'username':usrname})
    if request.method=='POST':
        topic=request.POST['topic']
        content=request.POST['content']
	date_str=request.POST['date']
	d=datetime.strptime(date_str,'%Y-%m-%d')
	date=d.date()
        blog=Blog(username=usrname,topic=topic,content=content,created=date)
        blog.save()
        return HttpResponse('/user/%s'%usrname)

#single post
def single_post(request,post_id):
    post_id=int(post_id)
    if request.method=='GET':
        blog=Blog.objects.get(id=post_id)
	cmnts=Comment.objects.filter(postId=post_id)
	return render_to_response('singlepost.html',{'post':blog,'cmnts':cmnts})
    if request.method=='POST':
        name=request.POST['name']
	body=request.POST['body']
        blog=Blog.objects.get(id=post_id)
	cmnt=Comment(name=name,body=body,postId=post_id)
        cmnt.save()
	return HttpResponse('/user/%s/%d/'%(blog.username,blog.id))

#logout
def usrlogout(request):
    logout(request)
    return HttpResponseRedirect("/")

#archive
def archive_view(request):
    if request.method=='GET':
        posts=Blog.objects.order_by("-created")
        return render_to_response('archive.html',{'posts':posts})

#postbyuser
def postbyuser(request,username):
    if request.method=="GET":
        posts=Blog.objects.filter(username=username)
	return render_to_response('viewpost.html',{'object_list':posts})

#post_view
def post_view(request,post_id):
    post_id=int(post_id)
    if request.method=='GET':
        blog=Blog.objects.get(id=post_id)
	cmnts=Comment.objects.filter(postId=post_id)
	return render_to_response('post_view.html',{'post':blog,'cmnts':cmnts})
    if request.method=='POST':
        name=request.POST['name']
	body=request.POST['body']
        blog=Blog.objects.get(id=post_id)
	cmnt=Comment(name=name,body=body,postId=post_id)
        cmnt.save()
	return HttpResponse('/post/%d/'%blog.id)
