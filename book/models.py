from django.db import models
from useraccount.models import user_account
# Create your models here.
class BookCategory(models.Model):
    category=models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.category

class Book(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    borrowing_price=models.DecimalField(max_digits=12, decimal_places=2)
    book_category=models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media/uploads/', blank = True, null = True)
    
    def __str__(self):
        return self.title

class BorrowBook(models.Model):
    user=models.ForeignKey(user_account, on_delete=models.CASCADE, null=True)
    book_title = models.CharField(max_length=100)
    book_description = models.TextField()
    book_price = models.DecimalField(max_digits=12, decimal_places=2)
    book_image = models.ImageField()
    book_category = models.CharField(max_length=100, blank=True, null=True)
    borrow_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_borrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.book_title
    
rating = (
    ('Not too bad', 'Not too bad'),
    ('Average', 'Average'),
    ('Good', 'Good'),
    ('Very Good', 'Very Good'),
    ('Excellent', 'Excellent')
)
class UserReview(models.Model):
    book= models.ForeignKey(Book, related_name="comments", on_delete=models.CASCADE, null=True)
    name= models.CharField(max_length=100,null=True)
    review_text = models.TextField(blank=True,null=True)
    is_borrowed = models.BooleanField(default=False)
    user_rating = models.CharField(max_length=20, choices=rating,null=True)
    def __str__(self):
        return str(self.name)