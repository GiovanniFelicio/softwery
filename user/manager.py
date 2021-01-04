from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .queryset import UserQuerySet


class UserManager(BaseUserManager):
    def create_user(self, login, name, password, email, is_active=False, is_staff=False, is_admin=False):
        if not login:
            raise ValueError('Login must be set!')
        user = self.model(login=login, email=email, name=name)
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, name, password, email):
        user = self.create_user(login, name, password, email, is_active=True, is_staff=True, is_admin=True)
        user.save(using=self._db)
        return user

    def get_queryset(self):
        return UserQuerySet(model=self.model, using=self._db, hints=self._hints)

    def list_users_by_company(self, company):
        return self.get_queryset().filter(company=company)

    def find_by_field_and_value(self, field, value):
        return self.get_queryset().raw("""
                                        SELECT id 
                                            FROM SFT_USER 
                                                WHERE %s = '%s'
                                        """ % (field, value))
