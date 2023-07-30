from django.http import HttpResponse
from django.urls import path
from . import views


urlpatterns = [
    path("",views.starting_page,name="starting-page"),
    path("posts",views.posts,name="posts-page"),
    path("posts/<slug:slug>",views.single_detail,name="post-detail-page") #posts/my-first-post (- sign is slug)
]

