from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('accounts/', views.index),
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    path('addvideos/', views.addvideos),
    path('videos/', views.videos),
    path('deletevideos/<int:myid>', views.deletevideos),
    path('editvideos/<int:myid>', views.editvideos),
    # path('settings/', views.settings),



    path('otherpages/', views.otherpages),

    path('addotherpages/', views.addotherpages),

    path('editotherpages/<int:myid>', views.editotherpages),

    path('deleteotherpages/<int:myid>', views.deleteotherpages),

    

    path('images/', views.images),

    path('addimages/', views.addimages),

    path('editimages/<int:myid>', views.editimages),

    path('deleteimages/<int:myid>', views.deleteimages),


    
    path('blog/', views.blog),

    path('addblog/', views.addblog),

    path('editblog/<int:myid>', views.editblog),

    path('deleteblog/<int:myid>', views.deleteblog),

    # path('post/<int:myid>', views.post),
    # path('delete/<int:myid>', views.delete),



   


    

]