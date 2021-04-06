#from django.shortcuts import render

from .models import Songs, Podcast, AudioBook
from .model_serializers import SongModelSerializer, PodcastModelSerializer, AudioBookModelSerializer
from rest_framework import generics

class SongData(generics.ListCreateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongModelSerializer

class PodcastData(generics.ListCreateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastModelSerializer

class AudibookData(generics.ListCreateAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookModelSerializer

# class ParticipantsData(generics.ListCreateAPIView):
#     queryset = Participants.objects.all()
#     serializer_class = ParticipantsModelSerializer

class SongDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongModelSerializer

class PodcastDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastModelSerializer

class AudibookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookModelSerializer

