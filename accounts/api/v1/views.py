from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import RegisterSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from .serializers import ChangePasswordSerializer






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
    
    
    
    


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })    
        
        
        
class Customdiscardauthtoken(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
class ChangePasswordApiView(generics.GenericAPIView):
    
    model = User
    permission_classes = [IsAuthenticated]    
    serializer_class = ChangePasswordSerializer
    
    def get_object(self, queryset = None):
        obj = self.request.user
        return obj
    
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data  = request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({'old_password':['wrong_pasword']},status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()

        
            return Response({'details ':'password changed'}, status=status.HTTP_200_OK )
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
       