from django import forms

from addrbook2.models import Entry


class CreateForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = (
            'created_by',
            'creation_time',
            'updated_by',
            'update_time',
        )


class EditForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = (
            'created_by',
            'creation_time',
            'updated_by',
        )
        widgets = {
            'update_time': forms.HiddenInput(),
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'country': forms.Textarea(attrs={'class': 'blue-background'}),
        }
        labels = {
            'children': '# of children',
            'phone_number': 'Phone #',
        }

