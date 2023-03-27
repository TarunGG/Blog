from django.urls import path
from .views import index, create_post, update_post,all_post,sngl_post,delete_post

urlpatterns = [
    path('',index,name='index'),
    path('create/', create_post, name='create'),
    path("create/<int:id>/",update_post,name="update post"),
    path("all/",all_post,name="all post"),
    path("all/<int:id>/",sngl_post,name="single post"),
    path("delete/<int:id>/",delete_post,name="delete post"),
    
]
