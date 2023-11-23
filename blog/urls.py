from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:no>/', views.detail, name='detail'),
    path("test1/", views.test1),
    path('test2/<no>/', views.test2),
    path('blog/profile/', views.profile),
    path('tag/<id>/', views.tag_list),
    path('test3/', views.test3),
    path('new/', views.post_create, name='create'),
    path('update/<id>/', views.post_update, name='update'),
    path('delete/<id>/', views.post_delete, name='delete'),
]

