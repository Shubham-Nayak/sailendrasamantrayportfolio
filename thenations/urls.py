from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='thenation/index.html', extra_context={
    #     "instagram_profile_name": "ishubhamnayak"
    # })),
    path('', views.index),

    path('about/', views.about),
    path('profile/', TemplateView.as_view(template_name='thenation/profile.html', extra_context={
        "instagram_profile_name": "sailendra.samantaray"
    })),

    path('videos/', views.videos),

    path('admin/', views.admin),
    path('saveform/', views.saveform),
    path('posts/<str:myurl>', views.posts),


    

]
