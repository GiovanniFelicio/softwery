from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,Permission,Group
from django.db.models import Q
from .manager import UserManager

class User(AbstractBaseUser,PermissionsMixin):

    REQUIRED_FIELDS = ['name', 'email', 'password']
    
    USERNAME_FIELD = 'login'
    
    name = models.CharField(name='name',max_length=100, null=False)
    email = models.EmailField(name='email',unique=True)
    login = models.CharField(name='login',max_length=30, null=False, unique=True)
    password = models.CharField(name='password',max_length=255,null=False)
    profile_photo = models.ImageField(name='profilePhoto',upload_to='profilePhotos', null=True, blank=True)
    date_birth = models.DateField(name='dateBirth',null=True)
    is_active = models.BooleanField(name='active',default=True)
    is_admin = models.BooleanField(name='is_admin',default=False)
    is_staff = models.BooleanField(name='is_staff', default=False)
    menus = models.ManyToManyField('menu.Menu', db_table='SFT_USER_MENU')
    company = models.ForeignKey(to='company.Company', on_delete=models.RESTRICT, null=True)
    groups = models.ManyToManyField( Group,
        verbose_name=('groups'),
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_name="user_set",
        related_query_name="user",
        db_table='SFT_USER_GROUP'
    )
    user_permissions = models.ManyToManyField(Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="user_set",
        related_query_name="user",
        db_table='SFT_USER_PERMISSION'
    )
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(name='createdAt',auto_now_add=True)
    updated_at = models.DateTimeField(name='updatedAt',auto_now_add=True)

    objects = UserManager()
    
    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        db_table = 'SFT_USER'
    
    def __str__(self):
        return self.name;
