from django.db import models

class Company(models.Model):
    
    name = models.CharField(max_length=100, null=False)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        db_table = 'SFT_COMPANY'