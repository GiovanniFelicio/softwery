from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .facade import CompanyFacade

@login_required
def listJson(request):
    companies = CompanyFacade._list(True)
    json = {"total": companies.count(), "results":""}    
    results = []
    for i in companies:
        result = {"id": i.id, "text": i.name}        
        results.append(result)
        
    json['results'] = results
        
    return JsonResponse(json)