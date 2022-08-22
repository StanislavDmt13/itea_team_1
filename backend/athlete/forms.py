
import datetime

from django import forms

from db.models import User


class AthleteEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birthday', 'phone', 'email']


class AthleteEditAvatar(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']


class CreateTrain(forms.Form):

    name = forms.CharField(
        required=True,
        max_length=120,
        help_text='''
        Only characters
        ''',
    )

    phone = forms.CharField(required=False, max_length=14)

    created_at = forms.DateTimeField(required=False, initial=datetime.datetime.now())