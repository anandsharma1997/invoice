
from django.contrib import admin
from django.urls import path
from .views import CreateInvoice, RetriveUpdateDeleteInvoice


urlpatterns = [
    path('invoice/', CreateInvoice.as_view()),
    path('invoice/<int:pk>/', RetriveUpdateDeleteInvoice.as_view()),

   
]
