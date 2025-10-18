from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(BaseUserCreationForm):
    """User creation form for admin interface."""

    class Meta:
        model = User
        fields = ("username", "email")


class UserChangeForm(forms.ModelForm):
    """User change form for admin interface."""

    class Meta:
        model = User
        fields = "__all__"


class UserSignupForm(forms.ModelForm):
    """User signup form for allauth."""

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")


class UserSocialSignupForm(forms.ModelForm):
    """User social signup form for allauth."""

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
