from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^article/$', views.ArticleList.as_view(), name='articles-list'),
    url(r'comments/$', views.CommentList.as_view(), name='comments-list'),
]