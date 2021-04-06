from django.urls import path
from . import views

urlpatterns = [
    path('api/songs/', views.SongData.as_view()),
    path('api/podcast/', views.PodcastData.as_view()),
    path('api/audiobook/', views.AudibookData.as_view()),
    path('api/songs_details/<int:pk>/', views.SongDetails.as_view()),
    path('api/podcast_details/<int:pk>/', views.PodcastDetails.as_view()),
    path('api/audiobook_details/<int:pk>/', views.AudibookDetails.as_view()),

]
