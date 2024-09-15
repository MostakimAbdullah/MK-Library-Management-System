from django import forms
from book.models import UserReview,rating
class ReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        exclude = ['is_borrowed','book','name']
