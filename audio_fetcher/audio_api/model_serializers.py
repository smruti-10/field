from rest_framework import serializers
from .models import Songs, Podcast, AudioBook

class SongModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('name', 'duration', 'uploaded_time')

class PodcastModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields= ('name', 'duration', 'uploaded_time', 'host', 'participants')

class AudioBookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ('title', 'author', 'narrator', 'duration', 'uploaded_time')

# class ParticipantsModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Participants
#         fields = '__all__'