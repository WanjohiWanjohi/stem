from django.urls import  path
from django.views.generic import TemplateView

urlpatterns = [
                       path('' , TemplateView.as_view(template_name='home.html') , name='home'),
                       path('blog' , TemplateView.as_view(template_name='blog.html') , name='blog'),
                       #not extended
                       path('join' , TemplateView.as_view(template_name='join.html') , name='join'),
                       path('project' , TemplateView.as_view(template_name='project.html') , name='project'),
                       path('implementation' , TemplateView.as_view(template_name='implementation.html') , name='implementation'),
                       path('labs' , TemplateView.as_view(template_name='labs.html') , name='labs'),
                       path('equipment' , TemplateView.as_view(template_name='equipment.html') , name='equipment'),
                       path('student' , TemplateView.as_view(template_name='student.html') , name='student'),
                       path('teacher' , TemplateView.as_view(template_name='teacher.html') , name='teacher'),
                       path('team' , TemplateView.as_view(template_name='team.html') , name='team'),
]