from django.urls import  path
from django.views.generic import TemplateView

urlpatterns = [
                       path('' , TemplateView.as_view(template_name='home.html') , name='home'),
                       path('blog' , TemplateView.as_view(template_name='blog.html') , name='blog'),
                       path('join' , TemplateView.as_view(template_name='join.html') , name='join'),
                       path('project' , TemplateView.as_view(template_name='project.html') , name='project'),
                       path('implementation' , TemplateView.as_view(template_name='implementation.html') , name='implementation'),
                       path('labs' , TemplateView.as_view(template_name='labs.html') , name='labs'),
                       path('stem' , TemplateView.as_view(template_name='stem.html') , name='stem'),
                       path('invention' , TemplateView.as_view(template_name='invention.html') , name='invention'),
                       path('coding' , TemplateView.as_view(template_name='coding.html') , name='coding'),
                       path('mobileapp' , TemplateView.as_view(template_name='mobileapp.html') , name='mobileapp'),
                       path('3d' , TemplateView.as_view(template_name='3d.html') , name='3d'),
                       path('competition' , TemplateView.as_view(template_name='competition.html') , name='competition'),
                       path('team' , TemplateView.as_view(template_name='team.html') , name='team'),
                       path('project/robotics' , TemplateView.as_view(template_name='robotics.html') , name='robotics'),
                       path('project/tinkering' , TemplateView.as_view(template_name='tinkering.html') , name='equipment'),
                       path('project/equipment' , TemplateView.as_view(template_name='equipment.html') , name='tinkering'),
                    #    path('project/invention' , TemplateView.as_view(template_name='robotics.html') , name='robotics'),

]