from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from .models import Topic, Room, Message
from userauth.models import User
from .forms import RoomForm
# Create your views here.


def study_room(request):
    page = 'study-room'
    search = request.GET.get('search') if request.GET.get('search') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=search) |
        Q(name__icontains=search) |
        Q(description__icontains=search)
        
        )
    
    topics = Topic.objects.all()
    room_count = rooms.count()
    
    
    context = {'page': page, 'topics': topics, 'rooms': rooms, 'room_count': room_count}
    return render(request, 'community/home.html', context)

def room(request, pk):
    page = 'study-room'
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        return redirect('room', pk=room.id)
    
    
    context = {'page': page, 'room': room, 'room_messages': room_messages}
    return render(request, 'community/room.html', context)

@login_required(login_url='login')
def createRoom(request):
    page = 'study-room'
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('study-room')
        
    context = {'form': form, 'page': page}
    return render(request, 'community/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    page = 'study-room'
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed here')
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('study-room')
        
    context = {'form': form, 'page': page}
    return render(request, 'community/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    page = 'study-room'
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed here')
    
    
    if request.method == 'POST':
        room.delete()
        return redirect('study-room')
    
    context = {'page': page, 'obj': room}
    return render(request, 'community/delete.html', context)