from django import forms
from django.contrib.auth.models import User


class RegistrarForm(forms.Form):

    first_name = forms.CharField(label='Nombres', required=True,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Nombres'
                                 }))

    last_name = forms.CharField(label='Nombres', required=True,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Apellidos'
                                }))

    username = forms.CharField(label='Usuario', required=True, min_length=6, max_length=30,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Nombre de usuario'
                               }))
    email = forms.EmailField(label='Correo electrónico', required=True,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'correo@email.com'
                             }))
    password = forms.CharField(label='Contraseña', required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Contraseña'
                               }))
    password2 = forms.CharField(label='Repetir contraseña', required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Repetir contraseña'
                                }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario ya existe')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Correo electrónico ya existe')

        return email

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'La contraseña no coincide')

    def GuardarUsuarios(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name')
        )
