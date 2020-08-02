from django import forms

from .models import Author


class AddArticleForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    title = forms.CharField(max_length=120)
    content = forms.CharField(widget=forms.Textarea(attrs={
        "col": "20",
        "row": "10",
        "placeholder": "Write article content here"
    }))