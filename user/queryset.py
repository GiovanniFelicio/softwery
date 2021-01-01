from django.db.models import Q
from django.db import models

class UserQuerySet(models.QuerySet):
    
    def listUsersByCompany(self,company):
        return (self.filter(company=company))