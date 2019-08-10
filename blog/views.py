from django.shortcuts import render,redirect
from .models import blog as blog_posts,blog_likes,blog_comments
from .forms import blog_form
from django.http import JsonResponse,HttpResponse
from  django.core.serializers import serialize,json
from django.utils.datastructures import MultiValueDictKeyError
from .serializers import blogSerializer,likeSerializer,commentSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.views.generic.base import TemplateView
from django.views import View
from rest_framework.generics import RetrieveAPIView 
from json import dumps,loads



# blog generic view
class BlogView(View):
    
    def get(self,request):
        posts = blog_posts.objects.all()
        
        serializeData = blogSerializer(posts,many=True)
       
        return JsonResponse(serializeData.data,safe=False)
        # return render(request,'blog.html')
    def post(self,request):
    
        if request.method == 'POST' and request.user.is_authenticated:
            post = blog_form(request.POST,request.FILES)
            obj = post.save(commit=False)
            user=request.user
            obj.user = User.objects.get(username=user)
            obj.save()
            data = blogSerializer(obj)
            # return JsonResponse(data.data,safe=False)
            return redirect('/blog')
       
def blog(request):
    return render(request,'blog.html',{'form':blog_form})
 

def deleteItem(request):
    id = request.POST['Id']
    post=blog_posts.objects.get(id=id)
    post.post_img.delete(False)
    post.delete()
    return HttpResponse("item deleted")

def edit(request):
    if(request.method == 'POST' ):
        id = request.POST['post_id']
        post = blog_posts.objects.get(id=id)
        post.post_title = request.POST['post_title']
        post.post = request.POST['post']
        try:
            img = request.FILES['post_img']
        except MultiValueDictKeyError:
            img = False
        if(img):
            post.post_img = img
            post.save()
            # blog_posts(update_fields=['post_title','post','post_img'])
        else:
           post.save()
            # blog_posts(update_fields=['post_title','post'])

        return redirect('/blog')
    return redirect('/blog')

class likes(View):
    def get(self,request):
        user = User.objects.get(username = request.user)
        likes = blog_likes.objects.all()
        likeData =likeSerializer(likes,many=True) 
        return JsonResponse(likeData.data,safe=False)   
    def post(self,request):
        post_id = blog_posts.objects.get(id=request.POST['id'])
        user = User.objects.get(username = request.user)
        postLike = blog_likes(post=post_id,user=user,like=True)
        postLike.save()
        return HttpResponse('liked')

class comments(View):
    def get(self,request):
        return HttpResponse("hi")
    def post(self,request):
        return HttpResponse('hi2')
