from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .helpers import CompanyHelper
from .models import Company
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializer import CompanySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class CompanyViewSet(viewsets.ViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication]

    def list(self, request):
        companies = Company.objects.list_companies(True)
        serializer = CompanySerializer(instance=companies, many=True)
        return Response(serializer.data)


@login_required
def listJson(request):
    companies = CompanyHelper._list(True)
    json = {"total": companies.count(), "results": ""}
    results = []
    for i in companies:
        result = {"id": i.id, "text": i.name}
        results.append(result)

    json['results'] = results

    return JsonResponse(json)
