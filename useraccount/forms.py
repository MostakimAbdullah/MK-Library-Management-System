from useraccount.models import user_account, user_address,GENDER_TYPE
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2','email','birth_date','gender','street_address','city','postal_code','country']

    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            birth_date = self.cleaned_data.get('birth_date')
            gender = self.cleaned_data.get('gender')
            street_address=self.cleaned_data.get('street_address')
            city=self.cleaned_data.get('city')
            postal_code=self.cleaned_data.get('postal_code') 
            country=self.cleaned_data.get('country')

            user_account.objects.create(
                user = our_user,
                birth_date = birth_date,
                gender = gender,
            )
            user_address.objects.create(
                user = our_user,
                street_address = street_address,
                city = city,
                postal_code = postal_code,
                country = country,
            )
            return our_user


class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=12, decimal_places=2)
