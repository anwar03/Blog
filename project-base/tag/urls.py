from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tag/$', views.TagListAPIView.as_view(), name='tag'),
    url(r'^tag/(?P<pk>\d+)/$',views.TagDetailsAPIView.as_view(), name='tag-details'),
    url(r'^tag/add/$',views.TagCreateAPIView.as_view(), name='add-tag'),
]