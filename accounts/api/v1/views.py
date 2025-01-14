from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import RegisterSerializer

class RegistraionApiView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'email':serializer._validated_data['email']
                
                
            }
            return Response(data , status = status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)