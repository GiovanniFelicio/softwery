from user.forms import form_create_user
from django.utils.safestring import mark_safe

def validate(form: dict):
    expected_form = form_create_user()
    
    errors = ''    
    
    fields = form.copy()
    
    for i in expected_form:
        options = expected_form[i]
        max_length = int(options['maxlength'])
        required = bool(options['required'])
        rstrip = bool(options['rstrip'])

        if i in fields:
            if len(fields[i]) <= 0 and required:
                errors += '* %s is required <br/>' %i
            elif max_length != -1 and len(fields[i]) > max_length:
                errors += '* Maximum allowed length for the %s field  %i characters <br/>' %(i,max_length)
                
            if rstrip:
                field = str(fields[i]).rstrip()
                fields[i] = field
        else:
            if required:
                errors += '* %s is required <br/>'%i                        
                
    return (fields,mark_safe(errors))