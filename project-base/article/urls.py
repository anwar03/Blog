from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.ArticleListAPIView.as_view(), name='articles-list'),
    url(r'^(?P<pk>\d+)/$', views.ArticleDetailsAPIView.as_view(), name='article-details'),
    url(r'^(?P<pk>\d+)/comments/$', views.CommentListAPIView.as_view(), name='comment-list'),
    url(r'^comment/(?P<pk>\d+)/$', views.CommentDetailsAPIView.as_view(), name='comment-details'),
    url(r'^comment/(?P<pk>\d+)/replys/$', views.ReplyListAPIView.as_view(), name='reply-List'),
    url(r'^reply/(?P<pk>\d+)/$', views.ReplyDetailsAPIView.as_view(), name='reply-details'),
]