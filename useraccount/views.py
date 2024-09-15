from django.shortcuts import render
from useraccount.forms import UserRegistrationForm,DepositForm
from django.shortcuts import redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from book.models import Book,BookCategory
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')

    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form, 'type': 'Register'})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            passwrd = form.cleaned_data['password']
            user = authenticate(username=name, password=passwrd)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'type': 'Login'})

@login_required
def Logoutview(request):
    logout(request)
    messages.success(request, 'Logout successfully.')
    return redirect('login')

def home(request, category_slug = None):
    books= Book.objects.all()
    if category_slug is not None:
        book_category= BookCategory.objects.get(slug=category_slug)
        books= Book.objects.filter(book_category=book_category)
    category=BookCategory.objects.all()
    return render(request, 'home.html', {'books': books, 'cat':category})


@login_required
def depositmoney(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            request.user.account.balance += amount
            request.user.account.save()
            messages.success(request, f'Deposit successful.')
            send_transaction_money(request.user, amount, "Deposit Money", "deposit_email.html")
            return redirect('home')
    else:
        form = DepositForm()
    return render(request, 'deposit_amount.html', {'form': form})


def send_transaction_money(user, amount, subject, template):
     message = render_to_string(template,{
          'user': user,
          'amount': amount,
     })
     send_email = EmailMultiAlternatives(subject, "", to = [user.email])
     send_email.attach_alternative(message, "text/html")
     send_email.send()
     