from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.ArticleList.as_view(), name='articles-list'),
    url(r'^(?P<pk>\d+)/$', views.ArticleDetails.as_view(), name='article-details'),
    url(r'^(?P<pk>\d+)/comments/$', views.CommentList.as_view(), name='comments-list'),
]