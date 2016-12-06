from django.conf.urls import *

#Django Rest Framework
from rest_framework import routers
from api import views
from django.views.decorators.csrf import csrf_exempt

#REST API routes
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
	url(r'^session', csrf_exempt(views.Session.as_view())),
	url(r'^register', csrf_exempt(views.Register.as_view())),
    url(r'^', include(router.urls)),
    #url(r'^api/', include('api.urls')),

    #Django Rest Auth
    url(r'^auth/', include('rest_framework.urls')),
]