from django.db.models import Q
from django.db import models

class CompanyQuerySet(models.QuerySet):

    def list_companies(self, active: bool):
        return self.filter(active=active).all()