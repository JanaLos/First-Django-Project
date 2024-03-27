from django import forms
from .models import Member
class MyForm(forms.Form):
    field1 = forms.CharField(label='Policko 1', max_length=100)
    field2 = forms.IntegerField(label='Policko 2')


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname']

class ConatctForm(forms.Form):
    field1 = forms.CharField(label='Policko 1', max_length=10)
    field2 = forms.IntegerField(label='Policko 2')