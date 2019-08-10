from django.forms import forms,ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm

# user form
class userRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1','password2']
    def __init__(self, *args, **kwargs):
        super(userRegisterForm,self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs={'class':'form-control','placeholder':'Enter First Name'}
        self.fields['last_name'].widget.attrs={'class':'form-control' ,'placeholder':'Enter last Name'}
        self.fields['username'].widget.attrs={'class':'form-control','placeholder':'Enter username'}
        self.fields['password1'].widget.attrs={'class':'form-control','placeholder':'Create password'}
        self.fields['password2'].widget.attrs={'class':'form-control','placeholder':'Conform password'}
       
        self.fields['username'].help_text=''
        self.fields['password1'].help_text=''
        self.fields['password2'].help_text=''

        self.fields['first_name'].label=''
        self.fields['last_name'].label=''
        self.fields['username'].label=''
        self.fields['password1'].label=''
        self.fields['password2'].label=''
    
