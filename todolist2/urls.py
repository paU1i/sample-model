from django.urls import path
from todolist2 import views

urlpatterns = [
    path('', views.home_action, name='todolist'),
    path('add-item', views.add_action, name='add-item'),
    path('delete-item/<int:item_id>', views.delete_action, name='delete-item'),
]
