from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status



@api_view(['GET','POST'])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST" :
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)




@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def postDetail(request,id):
    posts = Post.objects.get(pk=id)
    if request.method == "GET":
        try:
            serializer = PostSerializer(posts)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response('post dosnt exist', status=status.HTTP_404_NOT_FOUND)
    elif request.method == "PUT":
        serializer = PostSerializer(posts, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == "DELETE":
        posts.delete()
        return Response("item deleted")
