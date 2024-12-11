from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

        # Add secure input validation
        widgets = {
            'title': forms.TextInput(attrs={'required': True}),
            'content': forms.Textarea(attrs={'required': True}),
        }
