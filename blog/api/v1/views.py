from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post



@api_view()
def postList(request):
    return Response('ok')

@api_view()
def postDetail(request,id):
    posts = Post.objects.get(pk=id)
    serializer = PostSerializer(posts)
    return Response(serializer.data)
