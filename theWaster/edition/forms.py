from django import forms 
from django.contrib.auth.models import User

from edition.models import Edition, Sort, Article, Comment


class SortForm(forms.ModelForm):
    sort = forms.CharField(label='類別', max_length=64)


    class Meta: 
        model = Sort
        fields = '__all__'


class EditionForm(forms.ModelForm): 
    sort = forms.ModelChoiceField(label='類別',queryset=Sort)
    edition = forms.CharField(label='版名', max_length=128)
    user = forms.MultipleChoiceField(label='板主', queryset=User.objects) 

    class Meta: 
        model = Edition 
        fields = '__all__'
         

class ArticleForm(forms.ModelForm):
    edition = forms.ModelChoiceField(label='版別',queryset=Edition)
    title = forms.CharField(label='標題', max_length=128)
    content = forms.CharField(label='內容', widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ['edition', 'title', 'content']


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='內容', widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ['content']



