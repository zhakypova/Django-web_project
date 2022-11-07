from django.urls import path

from .views import greetings, ListItem, Detail


urlpatterns = [
    path('greetings/', greetings, name='greetings'),
    path('shop/', ListItem.as_view(), name = 'list_item'),
    path('shop/<int:pk>/', Detail.as_view(), name='detail_item'),
]


