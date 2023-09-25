from django import forms
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Name',
        widget=forms.TextInput(attrs={
            'class': "mt-1 block w-full rounded bg-gray-100 border-transparent focus:border-gray-500 focus:bg-white focus:ring-0",
            'placeholder': 'John Doe',
            'style': 'border: 1px solid #ccc'
        }),
        required=True
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
                                'class': "mt-1 block w-full rounded bg-gray-100 border-transparent focus:border-gray-500 focus:bg-white focus:ring-0",
                                'placeholder': "john@example.com",
                                'style': 'border: 1px solid #ccc'
                                }),
        required=True
    )
    subject = forms.CharField(
        max_length=100,
        label='Name',
        widget=forms.TextInput(attrs={
            'class': "mt-1 block w-full rounded bg-gray-100 border-transparent focus:border-gray-500 focus:bg-white focus:ring-0",
            'placeholder': 'Your subject',
            'style': 'border: 1px solid #ccc'
        }),
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': "mt-1 block w-full rounded bg-gray-100 border-transparent focus:border-gray-500 focus:bg-white focus:ring-0",
           
            'placeholder':"Your message...",
            'style': 'border: 1px solid #ccc',
            'rows': 7  # Change this value to adjust the height
        }),
        label='Message',
        required=True
    )

class SearchForm(forms.Form):
    query = forms.CharField()
    