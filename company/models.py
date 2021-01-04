from django.db import models
from .manager import CompanyManager

class Company(models.Model):
    
    name = models.CharField(max_length=100, null=False)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
        
    objects = CompanyManager()
    
    class Meta():
        db_table = 'SFT_COMPANY'
        permissions = [
            ('can_update_compnay', 'Allows the user to update the company')
        ]
        
    def __str__(self):
        return self.name