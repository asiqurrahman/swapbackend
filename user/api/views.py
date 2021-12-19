from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import User
from .serializers import UserSerializer
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username,
        token['avatar'] = str(user.avatar)
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 
@api_view(['GET'])
def getUser(request):
    user = User.objects.all()
    serializer = UserSerializer(user , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSingleUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user , many=False)
    return Response(serializer.data)

@api_view(['PATCH'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer
