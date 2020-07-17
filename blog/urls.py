from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostModelViewSet)
router.register(r'tags', views.TagModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]