from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, first_name,
                     last_name, is_staff, is_superuser, **extra_fields):
        """
        Create and save a User with the given email, password, name and
        phone number.

        :param email: string
        :param password: string
        :param first_name: string
        :param last_name: string
        :param is_staff: boolean
        :param is_superuser: boolean
        :param extra_fields:
        :return: User
        """
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, first_name, last_name,
                    password, **extra_fields):
        """
        Create and save a User with the given email, password and name.

        :param email: string
        :param first_name: string
        :param last_name: string
        :param password: string
        :param extra_fields:
        :return: User
        """
        return self._create_user(email, password, first_name, last_name,
                                 is_staff=False, is_superuser=False, **extra_fields)

    def create_superuser(self, email, first_name='',
                         last_name='', password=None, **extra_fields):
        """
        Create a super user.

        :param email: string
        :param first_name: string
        :param last_name: string
        :param password: string
        :param extra_fields:
        :return: User
        """
        return self._create_user(email, password, first_name, last_name,
                                 is_staff=True, is_superuser=True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model that represents an user.
    To be active, the user must register and confirm his email.
    """
    first_name = models.CharField(_('Nombre'), max_length=50)
    last_name = models.CharField(_('Apellido'), max_length=50)
    email = models.EmailField(_('Email'), unique=True)

    is_staff = models.BooleanField(_('Es staff'), default=False)
    is_superuser = models.BooleanField(_('Es superusuario'), default=False)
    is_active = models.BooleanField(_('Activo'), default=True)

    date_joined = models.DateTimeField(
        _('Fecha de ingreso'), auto_now_add=True)
    date_updated = models.DateTimeField(_('Último ingreso'), auto_now=True)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        """
        Unicode representation for an user model.
        :return: string
        """
        return self.email

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        :return: string
        """
        return "{0} {1}".format(self.first_name, self.last_name)

    def get_short_name(self):
        """
        Return the first_name.
        :return: string
        """
        return self.first_name

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
