from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class UserManager(BaseUserManager):
    # my method to create user with the 2 major data
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("user must provide a valid email")
        if not username:
            raise ValueError("user must provide a valid username")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email=email, username=username, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=105, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    level = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()


class Tests(models.Model):
    student_user = models.ForeignKey(
        User, related_name="test_history", on_delete=models.CASCADE)
    question_pointers = ArrayField(models.IntegerField())
    date = models.DateTimeField()
    score = models.CharField(max_length=5)
