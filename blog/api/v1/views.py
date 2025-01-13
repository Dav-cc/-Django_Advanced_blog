from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListCreateAPIView
from rest_framework import mixins




# @api_view(['GET','POST'])
# def postList(request):
#     if request.method == "GET":
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST" :
#         serializer = PostSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(request.data)
'''

class PostList(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get (self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
'''


class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()






class PostSingle(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    # def get(self , request, *args, **kwargs):
    #     return self.retrieve( request, *args, **kwargs)

    # def put(self ,request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)






'''

class PostSingle(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer


    def get(self,request, id):
        post = Post.objects.get(pk = id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self , request , id):
        post = Post.objects.get(pk = id)
        serializer = PostSerializer(post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id):
        post = Post.objects.get(pk = id)
        post.delete()
        return Response("item deleted")

'''














# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
# def postDetail(request,id):
#     posts = Post.objects.get(pk=id)
#     if request.method == "GET":
#         try:
#             serializer = PostSerializer(posts)
#             return Response(serializer.data)
#         except Post.DoesNotExist:
#             return Response('post dosnt exist', status=status.HTTP_404_NOT_FOUND)
#     elif request.method == "PUT":
#         serializer = PostSerializer(posts, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#     elif request.method == "DELETE":
#         posts.delete()
#         return Response("item deleted")


# class Postviewset(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     lookup_field = 'id'
    
#     def list(self , request):
#         query = Post.objects.all()
#         serializer = self.serializer_class(self.queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         queryset = get_object_or_404(self.queryset , pk=pk)
#         serializer = self.serializer_class(queryset)
#         return Response(serializer.data)
        
        