
from django import forms

from db.models import User, Train


class AthleteEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birthday', 'phone', 'email']


class TrainEditForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ['title', 'description', 'image', 'author', 'train_program']


class AthleteEditAvatar(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']


class NewTrainForm(forms.ModelForm):

    class Meta:
        model = Train
        fields = ['title', 'description', 'image', 'author', 'train_program']
