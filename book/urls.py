from django.urls import path
from django.views.generic import *
from .models import Book #book앱에 models에 Book 모델 만든 거 가져오기. 
from django.urls import reverse, reverse_lazy

app_name='book'

urlpatterns = [
    path("", ListView.as_view(model=Book), name='list'),
    path('detail/<pk>/', DetailView.as_view(model=Book), name='detail'),
    path('create/', CreateView.as_view(model=Book, fields='__all__'), name='create'),
    path('update/<pk>/', UpdateView.as_view(model=Book, fields='__all__'), name='update'),
    path('delete/<pk>/', DeleteView.as_view(model=Book, success_url=reverse_lazy('book:list')), name='delete'),
    
]