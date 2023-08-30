from django import forms
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
            'placeholder': 'Name',
            'style': 'border: 1px solid #ccc'
        }),
        required=True
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
                                'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
                                'placeholder': 'Email',
                                'style': 'border: 1px solid #ccc'
                                }),
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
            'placeholder': 'Message',
            'style': 'border: 1px solid #ccc',
            'rows': 4  # Change this value to adjust the height
        }),
        label='Message',
        required=True
    )