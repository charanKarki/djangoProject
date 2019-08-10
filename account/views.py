from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.views import LoginView
from django.views import View
from .forms import userRegisterForm

# Create your views here.


# django user sign up view


class signupView(View):
    template_name='signup.html'
    def get(self,request):
        return render(request,self.template_name,{'form':userRegisterForm})

    def post(self,request):
        user = userRegisterForm(request.POST)
        if(user.is_valid()):
            user.save()
            user = User.objects.get(username=request.POST['username'])
            auth.login(request,user)
            return redirect('/')
        else:
            return render(request,'signup.html')
            


#  django view for user login       
class LoginView(LoginView):

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html',{'msg':'user does not exist try again','class':'danger'})
        
        return render(request,'login.html',{'title':'LogIn page'})

