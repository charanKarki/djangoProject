from django.urls import path
from .views import signupView,LoginView 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/',signupView.as_view(),name='signup'),
    path('login/',LoginView.as_view(
        template_name='login.html'
    ),name='login'),
    path('logout/',LogoutView.as_view(next_page='/'),name='logout')
]
