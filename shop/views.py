from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.views import generic

from .models import Item, Purchase


def greetings(request):
    return HttpResponse("Добро пожаловать в наш магазин!")

class ListItem(generic.ListView):
    model = Item
    template_name = 'list_item.html'
    context_object_name = 'items'

class Detail(generic.DetailView):
    model = Item
    template_name = 'detail_item.html'
    context_object_name = 'item'
