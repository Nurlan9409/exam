from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import ArtisAPIViewSet,AlbumAPIViewSet,SongAPIViewSet
router = DefaultRouter()
router.register('artist',ArtisAPIViewSet)
router.register('album',AlbumAPIViewSet)
router.register('song',SongAPIViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('',include(router.urls)),
    path('',include(router.urls)),

]
