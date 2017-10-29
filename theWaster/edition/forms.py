from django import forms 
from django.contrib.auth.models import User
from edition.models import Edition


class EditionForm(forms.ModelForm): 
    editionName = forms.CharField(label='版名', max_length=128)
    press = forms.ModelChoiceField(label='板主', queryset=User.objects) 
     
#     def __init__(self, *args, **kwargs): 
#         relateds = kwargs.pop('related', None) 
#         super(NewsForm, self).__init__(*args, **kwargs) 
#         self.fields['related'].queryset = relateds 
    
    class Meta: 
        model = Edition 
        fields = '__all__'
         
