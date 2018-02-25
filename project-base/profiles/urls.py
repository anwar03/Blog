from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('user-profile', views.UserProfileViewSet, base_name='user-profile')
router.register('login', views.LoginViewSet, base_name='login')


urlpatterns = [
    url(r'',include(router.urls)),
]