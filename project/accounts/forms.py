# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    nickname = forms.CharField(max_length=30, required=True, help_text="Обов'язкове поле. Відображатиметься публічно.")
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Підтвердіть пароль")

    class Meta:
        model = CustomUser
        fields = ('nickname', 'email', 'first_name', 'last_name')

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        if CustomUser.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError("Користувач з таким нікнеймом вже існує.")
        return nickname

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Користувач з таким email вже зареєстрований.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Паролі не співпадають.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user