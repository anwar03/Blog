from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('user-profile', views.UserProfileViewSet, base_name='user-profile')

urlpatterns = [
    #url(r'^user-profile/$', views.UserProfileViewSet, name='user-profile'),
    url(r'',include(router.urls)),
]