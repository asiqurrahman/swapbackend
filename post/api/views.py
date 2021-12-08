from rest_framework.response import Response
from rest_framework.decorators import api_view
from post.models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def getPost(request):
    post = Post.objects.all().order_by('-date_posted')
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)

@api_view(['Post'])
def createPost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PATCH'])
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)