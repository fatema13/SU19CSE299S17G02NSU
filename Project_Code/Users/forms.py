from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# this file  inherits the exisitng register form so that we can add extra fields
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
         model = User
         fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']












TRUE_FALSE_CHOICES = (
    ('Horror', 'Horror'),
    ('novel', 'novel'),
    ('Science Fiction', 'Science Fiction'),
    ('Speculative fiction', 'Speculative fiction'),
    ('Fiction', 'Fiction'),
    ('Mystery', 'Mystery'),
    ('Crime Fiction', 'Crime Fiction'),
    ('Thriller', 'Thriller'),
    ('Fantasy', 'Fantasy'),
    ('Historical fiction', 'Historical fiction'),
    ('Satire', 'Satire'),
    ('Autobiography', 'Autobiography'),
    ('Non-fiction', 'Non-fiction'),
    ('Autobiographical movel', 'Autobiographical movel'),
    ('History', 'History'),
    ('Biography', 'Biography'),
    ('Western', 'Western'),
    ('Romance novel', 'Romance novel'),

)



class MyLibraryUpdateForm(forms.Form):


    user = forms.CharField(max_length=11,)
    name = forms.CharField(label="Phone Number*", max_length=11,)
    author = forms.CharField(label="Business Name*")


    genre = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label="Do you have a TIN?*",
                              initial='', widget=forms.Select(), required=True)

    # do_you_have_a_TIN.widget = forms.ChoiceField(attrs={'size': 45,})
