from django import forms
from django.contrib.auth import get_user_model

from web.models import MoneySlot

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    repassword = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['repassword']:
            self.add_error('password', 'Пароли не совпадают')
        return cleaned_data

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'repassword')


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class MoneySlotForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)

    class Meta:
        model = MoneySlot
        fields = ('title', 'amount_spent')

