from django.urls import path
from .views import (
                blog,
                BlogView,
                deleteItem,
                edit,
                likes,
                comments )
# urls 
urlpatterns = [
    path('blog/',blog,name='blog'),
    path('showposts/',BlogView.as_view()),
    # path('show_post/',show_post),
    path('deleteItem/',deleteItem),
    path('edit/',edit),
    path('likes/',likes.as_view()),
    path('comment/',comments.as_view()),
   
]
