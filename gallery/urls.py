from django.urls import path
from django.views.generic import TemplateView

app_name = 'gallery'
urlpatterns = [
    path('', TemplateView.as_view(template_name='gallery/gallery_list.html'), name='image_list'),
    
    
]