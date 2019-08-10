from django.urls import path
from .views import home


# url patterns
urlpatterns = [
    path('',home,name='home')
]
