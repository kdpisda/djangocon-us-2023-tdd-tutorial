from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model."""

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
