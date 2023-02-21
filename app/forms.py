from django import forms
from app import models


class BSForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class EnvForm(BSForm):
    class Meta:
        model = models.Env
        fields = '__all__'


class ServiceForm(BSForm):
    class Meta:
        model = models.Service
        fields = '__all__'


class PasswordForm(BSForm):
    class Meta:
        model = models.Password
        fields = '__all__'
