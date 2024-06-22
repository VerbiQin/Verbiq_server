from django.shortcuts import render
from django.http import HttpResponse
from .serializers import NoteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TextNote

@api_view(['GET'])
def index(request):
    sort_param = request.GET.get('sort', 'random') 
    search_param = request.GET.get('search', '')

    # Filter notes based on search_param
    if search_param:
        notes = TextNote.objects.filter(content__icontains=search_param)
    else:
        notes = TextNote.objects.all()

    # Sort notes based on sort_param
    if sort_param == 'recent':
        notes = notes.order_by('-created_at')  # Sort by descending created_at
    elif sort_param == 'oldest':
        notes = notes.order_by('created_at')   # Sort by ascending created_at
    elif sort_param == 'random':
        notes = notes.order_by('?')            # Randomize order (not efficient for large datasets)

    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def postnote(request):
    data = request.data
    note_data = {
        'content': data.get('content'),
    }
    print(note_data)
    serializer = NoteSerializer(data=note_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

