from django.db import models
from django import forms


class User(models.Model):
    user_email = models.CharField('user email',max_length=130)
    user_name = models.CharField('username',max_length=255)
    user_password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    user_signup_date = models.DateTimeField('date of signup')

    def __str__(self):
        return self.user_email