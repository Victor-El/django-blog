from django import forms

from .models import Author, Article


class AddArticleForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={
        "placeholder": "title"
    }))
    content = forms.CharField(label="", widget=forms.Textarea(attrs={
        "col": "20",
        "row": "10",
        "placeholder": "Write article content here"
    }))


    def persist(self, user):
        data = self.cleaned_data
        user = user
        print(data)
        print(data)
        Article.objects.create(author=user, title=data['title'], content=data['content'])
        return True


    def clean(self):
        if len(self.cleaned_data.get("content")) < 20:
            raise forms.ValidationError("Content too short")
        else:
            return self.cleaned_data