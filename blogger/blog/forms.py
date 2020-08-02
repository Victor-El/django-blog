from django import forms

from .models import Author, Article


class AddArticleForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    title = forms.CharField(max_length=120)
    content = forms.CharField(widget=forms.Textarea(attrs={
        "col": "20",
        "row": "10",
        "placeholder": "Write article content here"
    }))


    def persist(self):
        data = self.cleaned_data
        print(data)
        print(data)
        Article.objects.create(author=data['author'], title=data['title'], content=data['content'])
        return True


    def clean(self):
        if len(self.cleaned_data.get("content")) < 20:
            raise forms.ValidationError("Content too short")
        else:
            return self.cleaned_data