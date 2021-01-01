from .models import Company

class CompanyFacade():
    
    @staticmethod
    def _list(active=False):
        return Company.objects.listCompanies(active)