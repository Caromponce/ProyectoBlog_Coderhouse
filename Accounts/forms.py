from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')


    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name'] 


class changePasswordForm(PasswordChangeForm):
    old_password  = forms.CharField(widget=forms.PasswordInput, label='Password actual')
    new_password1 = forms.CharField(widget=forms.PasswordInput, label='Password nuevo')
    new_password2 = forms.CharField(widget=forms.PasswordInput, label='Password')
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:'' for k in fields}
