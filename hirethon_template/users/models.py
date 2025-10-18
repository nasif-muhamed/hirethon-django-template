from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, DateTimeField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from hirethon_template.users.managers import UserManager


class User(AbstractUser):
    """
    Default custom user model for hirethon-template.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    username = CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = EmailField(_("email address"), unique=True)
    created_at = DateTimeField(_("created at"), default=timezone.now, editable=False)
    updated_at = DateTimeField(_("updated at"), auto_now=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"pk": self.id})
