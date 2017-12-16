from django.contrib.auth.models import AbstractUser, UserManager

from unicom.settings import ADMIN_GROUP


class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        extra_fields.pop('is_staff')
        return super()._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    objects = CustomUserManager()

    @property
    def is_staff(self):
        is_active_admin = (self.groups.filter(name=ADMIN_GROUP).exists() and
                           self.is_active)
        return self.is_superuser or is_active_admin
