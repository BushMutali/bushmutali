from django.shortcuts import render
from .models import Topic, Room, Message
from userauth.models import User
# Create your views here.


def study_room(request):
    page = 'study-room'
    
    topics = Topic.objects.all()
    rooms = Room.objects.all()
    
    context = {'page': page, 'topics': topics, 'rooms': rooms}
    return render(request, 'community/home.html', context)

def room(request, pk):
    page = 'study-room'
    room = Room.objects.get(id=pk)
    messages = Message.objects.all()
    context = {'page': page, 'room': room, 'messages': messages}
    return render(request, 'community/room.html', context)