from django.urls import path
from website import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('login/index/',views.index,name='index'),
    path('login/index/home/',views.home,name='home'),
    path('index/home/',views.home,name='home'),
    path('index/',views.index,name='index'),

]
