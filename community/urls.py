from django.urls import path
from . import views

urlpatterns = [
    path('community/', views.study_room, name="study-room"),
    path('community/room/<str:pk>/', views.room, name='room'),
]
