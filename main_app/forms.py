from django import forms
from .models import Finch

class FinchForm(forms.ModelForm):
    class Meta:
        model = Finch
        fields = '__all__'


class FinchDeleteForm(forms.ModelForm):
    class Meta:
        model = Finch
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['confirm_delete'] = forms.BooleanField(required=True, initial=False,
                                                           label='Are you sure you want to delete this Finch?')

