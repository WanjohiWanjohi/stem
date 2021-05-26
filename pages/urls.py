from django.urls import  path
from django.views.generic import TemplateView

urlpatterns = [
                       path('' , TemplateView.as_view(template_name='home.html') , name='home'),
                       path('/blog' , TemplateView.as_view(template_name='blog.html') , name='blog'),
                       path('' , TemplateView.as_view(template_name='home.html')),
                       path('' , TemplateView.as_view(template_name='home.html')),
                       path('' , TemplateView.as_view(template_name='home.html')),
]