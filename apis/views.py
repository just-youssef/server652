from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import filters


class جنودViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Note instances.
    """
    serializer_class = جنودSerializer
    queryset = جنود.objects.all()

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["رقم_عسكرى", "اسم"]
    ordering = ['رقم_عسكرى']

class ضباطViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Note instances.
    """
    serializer_class = ضباطSerializer
    queryset = ضباط.objects.all()

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields =  ["رقم_الأقدمية", "اسم"]
    ordering = ['رقم_الأقدمية']


class ضباط_صفViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Note instances.
    """
    serializer_class = ضباط_صفSerializer
    queryset = ضباط_صف.objects.all()

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["رقم_عسكرى", "اسم"]
    ordering = ['رقم_عسكرى']
