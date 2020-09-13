from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


class AuthUserManager(UserManager):
    def create_user(self, email=None, password=None, **kwargs):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user)
        return user

    def create_superuser(self, email=None, password=None, **kwargs):
        user = self.create_user(email=email, password=password, is_admin=True)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = AuthUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    fullname = models.CharField(max_length=100, null=True)
    profile_pix = models.ImageField(upload_to='profile_pix', default='profile_pix/default.png')