from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='thenation/index.html', extra_context={
    #     "instagram_profile_name": "ishubhamnayak"
    # })),
    path('', views.index),

    path('about/', views.about),
 
    path('profile/',views.profile),

    path('home/', views.home, name='home'),

    path('videos/', views.videos),
    path('blogs/', views.blogs),
    path('blog/<int:myid>', views.blog),



    path('admin/', views.admin),
    path('saveform/', views.saveform),
    


    

]
