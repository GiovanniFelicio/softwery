from .models import Company

class CompanyHelper():
    
    @staticmethod
    def _list(active=False):
        return Company.objects.listCompanies(active)
