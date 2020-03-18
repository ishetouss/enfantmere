from django import forms
from .models import Blog





class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
    
    class Meta():
        model = Blog
        fields = ['author', 'body',]
        


class SendMessageForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "enter your name"
        })
    )
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": " plz Enter your Email or phone"
        }
    ))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "plz Leave a message"
        }
    ))
