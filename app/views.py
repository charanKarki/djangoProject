from django.shortcuts import render
from blog.models import blog 
# Create your views here.

def home(request):
    posts = blog.objects.all()
    return render(request,'home.html',{'title':'Home','posts':posts})