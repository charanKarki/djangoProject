from django.forms import forms,ModelForm
from .models import blog


class blog_form(ModelForm):
   
    class Meta:
        model=blog
        fields=['post_title','post','post_img']
    def __init__(self, *args, **kwargs):
        super(blog_form,self).__init__(*args, **kwargs)
        self.fields['post_title'].widget.attrs={'class':'form-control','placeholder':'Post Title'}
        self.fields['post'].widget.attrs={'class':'form-control','col':'30','row':'10'}
        self.fields['post_img'].widget.attrs={'class':' custom-file-input'}
        self.fields['post_img'].label=''
