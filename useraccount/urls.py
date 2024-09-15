from django.urls import path
from useraccount.views import RegisterView,LoginView,Logoutview,home,depositmoney

urlpatterns =[
    path('register/', RegisterView , name='registration'),
    path('login/', LoginView , name='login'),
    path('logout/', Logoutview , name='logout'),
    path('home/', home, name='home'),
    path('category/<slug:category_slug>', home , name='category_wise_slug'),
    path('deposit/', depositmoney , name='Deposit'),
]