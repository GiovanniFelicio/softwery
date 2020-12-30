from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, login, name, password, email, is_active=False, is_staff=False, is_admin=False):
        if not login:
            raise ValueError('Login must be set!')
        user = self.model(login=login, email=email, name=name)
        user.is_active=is_active
        user.is_staff=is_staff
        user.is_admin=is_admin
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, name, password, email):
        user = self.create_user(login, name, password, email,is_active=True, is_staff=True, is_admin=True)
        user.save(using=self._db)
        return user    

class User(AbstractBaseUser):

    REQUIRED_FIELDS = ['name', 'email', 'password']
    
    USERNAME_FIELD = 'login'
    
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True)
    login = models.CharField(max_length=30, null=False, unique=True)
    password = models.CharField(max_length=255,null=False)
    profile_photo = models.ImageField(upload_to='profilePhotos', null=True, blank=True)
    date_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = UserAccountManager()
    
    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        db_table = 'SFT_USER'
    
    def __str__(self):
        return self.name;