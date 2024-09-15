from django.shortcuts import render,redirect
from book.models import Book,BorrowBook,UserReview
from useraccount.models import user_account,User
from django.contrib import messages
from book.forms import ReviewForm
from django.template.loader import render_to_string
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
# Create your views here.
def send_transaction_email(user, book, subject, template):
     message = render_to_string(template,{
          'user': user,
          'book': book,
     })
     send_email = EmailMultiAlternatives(subject, "", to = [user.email])
     send_email.attach_alternative(message, "text/html")
     send_email.send()
     
@login_required
def Book_detail(request,id):
        book = Book.objects.get(pk=id)
        has_borrowed = False
        has_borrowed = BorrowBook.objects.filter(user=request.user.account,book_title = book.title,is_borrowed=True).exists()
 
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid(): 
                review_text = form.cleaned_data['review_text']
                user_rating = form.cleaned_data['user_rating']
            
                # review, created = UserReview.objects.update_or_create(
                #     book=book,  
                #     defaults={
                #         'review_text': review_text,
                #         'user_rating': user_rating,
                #         'is_borrowed': True  
                #     }
                # )
                UserReview.objects.create(
                    book=book,
                    name=request.user.username,  
                )
                UserReview.objects.filter(book=book,name=request.user.username).update( review_text=review_text, user_rating=user_rating)
                form.save(commit=False)
                messages.success(request, 'Review submitted successfully.')
        else:
                form = ReviewForm()

        review=UserReview.objects.filter(book=book)
        return render(request, 'books_details.html', {'book':book, 'form': form,'cmt': review, 'borrow': has_borrowed})


@login_required
def buy_book(request,id=None):
    if id is not None:
        newBook=Book.objects.get(pk=id)
        if request.user.account.balance > newBook.borrowing_price:
            request.user.account.balance-=newBook.borrowing_price
            request.user.account.save()
            review=UserReview(book=newBook, is_borrowed=True)
            review.save()
            # user=User.objects.all()
            # for i in user:
            #      if i.username==request.user.username:
            #          name=i.username
            BorrowBook.objects.create(
                user=request.user.account,    
                book_title = newBook.title,
                book_description = newBook.description,
                book_price = newBook.borrowing_price,
                book_image = newBook.image.url,
                book_category = newBook.book_category,
                is_borrowed = True
            )
            # BorrowBook.objects.filter(book_title=newBook.title).create(user=name)
            messages.success(request, 'Book borrowed successfully.')
            send_transaction_email(request.user, newBook.title, "Borrowd Book", "borrowed_books.html")
        else:
            messages.error(request, 'Insufficient balance.')
    book = BorrowBook.objects.filter(user=request.user.account)
    return render(request, 'profile.html', {'book': book})

@login_required       
def return_book(request,id):
    book=BorrowBook.objects.get(pk=id)
    book.is_borrowed=False
    book.save()
    request.user.account.balance+=book.book_price
    request.user.account.save()
    messages.success(request, 'Book returned successfully.')
    return redirect('profile')