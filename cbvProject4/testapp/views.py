from django.shortcuts import render
from testapp.models import Bikes
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

class BikelistView(ListView):
    model=Bikes

class BikedetailView(DetailView):
    model=Bikes

class BikecreateView(CreateView):
    model=Bikes
    fields='__all__'

class BikeupdateView(UpdateView):
    model=Bikes
    fields=['engine','milage','price']

from django.urls import reverse_lazy
class BikedeleteView(DeleteView):
    model=Bikes
    success_url=reverse_lazy('list')
