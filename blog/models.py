from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # username= models.CharField(max_length=20)
    post_title = models.CharField(max_length=50)
    post = models.TextField()
    post_img = models.ImageField(upload_to='post_img', default='default.jpg',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'this is {self.user} blog post'


# for likes in post
class blog_likes(models.Model):
    post = models.ForeignKey(blog,on_delete=models.CASCADE) #delete whole likes when post is deleted
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True) #set user to null when user is deleted
    like = models.BooleanField()
    def __str__(self):
        return f'{self.post} post likes '
    


    
# for comments in post 
class blog_comments(models.Model):
    post = models.ForeignKey(blog,on_delete=models.CASCADE) #when post is deleted comments also deleted
    comment = models.TextField(null=True)
    def __str__(self):
        return f'{self.post} post comments '