from django.db.models import Q
from django.db import models

class CompanyQuerySet(models.QuerySet):

    def listCompanies(self, active: bool):
        return self.filter(active=active).all()