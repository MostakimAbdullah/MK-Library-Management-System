from django.contrib import admin
from book.models import Book,BookCategory,BorrowBook,UserReview
# Register your models here.

class BookSlugField(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category',)}
    list_display = ['category','slug']

admin.site.register(BookCategory, BookSlugField)
admin.site.register(Book)
admin.site.register(BorrowBook)
admin.site.register(UserReview)