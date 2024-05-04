from django.shortcuts import render
from music.models import Artist, Album, Song
from music.serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from rest_framework import viewsets



class ArtisAPIViewSet(viewsets.ModelViewSet):
    queryset =Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumAPIViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongAPIViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
