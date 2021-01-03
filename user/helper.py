from .models import User
from company.models import Company

class UserHelper():
    
    @staticmethod
    def find_by_field_and_value(field: str, value: str):
        return User.objects.find_by_field_and_value(field, value)
    
    @staticmethod
    def generate_and_create_user(fields: dict):
        user = User()        
        
        if len(fields) > 0:
            user.name = fields['name']
            user.email = fields['email']
            user.login = fields['login']
            user.number = fields['number']
            user.date_birth = fields['dateBirth']
            
            company = Company.objects.filter(pk=int(fields['company'])).first()
            
            user.company = company
            user.set_password(fields['password'])
            
        user.save()            
            

        