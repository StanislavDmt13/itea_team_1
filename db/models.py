from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

'''
documentation fields: https://docs.djangoproject.com/en/4.0/ref/models/fields/
'''


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """
        Create and return a `User` with an email, phone number, username and password.
        """
        if not email:
            raise ValueError("Users must have an email.")

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if not password:
            raise ValueError("Superusers must have a password.")
        if not email:
            raise ValueError("Superusers must have an email.")

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=50, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to="users", null=True, blank=True)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email


class Articles(models.Model):
    title = models.CharField(max_length=200)
    intro_article = models.TextField(blank=False)
    article = models.TextField(blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TrainProgram(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name='programs', on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=200)
    descriptions = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Train(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="users", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    train_program = models.ForeignKey(TrainProgram, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
