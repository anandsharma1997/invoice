from django.shortcuts import render
from rest_framework import generics
from .models import Invoice, InvoiceDetail
from .serialiazers import InvoiceSerializer, InvoiceDetailSerializer

# Create your views here.


class CreateInvoice(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class RetriveUpdateDeleteInvoice(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer

