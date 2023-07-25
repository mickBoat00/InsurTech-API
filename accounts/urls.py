from django.urls import path

from .views import login, logout, signup

urlpatterns = [
    path('signup/', signup.as_view(), name='signup'),
    path('login/', login.as_view(), name='login'),
    path('logout/', logout.as_view(), name='logout'),
]