from django.urls import path
from book.views import Book_detail,buy_book,return_book
urlpatterns =[
    path('books/<int:id>', Book_detail , name='details'),
    path('profile_page/', buy_book , name='profile'),
    path('buy/<int:id>', buy_book , name='buy'),
    path('return_book/<int:id>', return_book , name='return'),
]