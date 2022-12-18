from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers  import CountrySerializer
from .models import Country
from .permissions import OwnerOnly
from rest_framework.permissions import IsAuthenticated


class CountryListView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]


class CountryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [OwnerOnly, IsAuthenticated]
