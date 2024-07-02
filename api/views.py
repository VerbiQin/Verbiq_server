from django.shortcuts import render
from django.http import HttpResponse
from .serializers import NoteSerializer,CommentReplaySerializer,CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TextNote,CommentReplay,Comment

@api_view(['GET'])
def index(request):
    sort_param = request.GET.get('sort', 'random') 
    search_param = request.GET.get('search', '')
    if search_param:
        notes = TextNote.objects.filter(content__icontains=search_param)
    else:
        notes = TextNote.objects.all()
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


@api_view(['GET'])
def display_comment(request, note_id):
    filter_option = request.GET.get('filter', 'recent')
    try:
        if filter_option == 'recent':
            comments = Comment.objects.filter(note_id=note_id).order_by('-created_at')
        elif filter_option == 'oldest':
            comments = Comment.objects.filter(note_id=note_id).order_by('created_at')
        elif filter_option == 'random':
            comments = Comment.objects.filter(note_id=note_id).order_by('?')
        else:
            comments = Comment.objects.filter(note_id=note_id)
        
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['POST'])
def post_comment(request,note_id):
    newComment = request.data.get('comment')
    try:
        note = TextNote.objects.get(pk=note_id)
    except TextNote.DoesNotExist:
        return Response({"error": "Note does not exist"}, status=status.HTTP_404_NOT_FOUND)
    data = {
        'note': note_id,
        'content':newComment,
    }
    serializer = CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def display_comment_replay(request, comment_id):
    replay = CommentReplay.objects.filter(comment=comment_id)
    serializer = CommentReplaySerializer(replay, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_comment_replay(request, comment_id):
    new_comment = request.data.get('comment')
    try:
        comment = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        return Response({"error": "Comment does not exist"}, status=status.HTTP_404_NOT_FOUND)

    data = {
        'comment': comment.id,  # use the comment ID for foreign key
        'content': new_comment,
    }

    serializer = CommentReplaySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
