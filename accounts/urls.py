from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('accounts/', views.index),
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    path('otherpages/', views.otherpages),
    path('addvideos/', views.addvideos),
    path('videos/', views.videos),
    path('deletevideos/<int:myid>', views.deletevideos),
    path('editvideos/<int:myid>', views.editvideos),
    # path('settings/', views.settings),




    path('addotherpages/', views.addotherpages),

    path('editotherpages/<int:myid>', views.editotherpages),

    path('deleteotherpages/<int:myid>', views.deleteotherpages),

    # path('post/<int:myid>', views.post),
    # path('delete/<int:myid>', views.delete),



   


    

]