from django.urls import path
from addrbook2 import views

urlpatterns = [
    path('', views.search_action, name='home'),
    path('search', views.search_action, name='search'),
    path('create', views.create_action, name='create'),
    path('delete/<int:id>', views.delete_action, name='delete'),
    path('edit/<int:id>', views.edit_action, name='edit'),
]

