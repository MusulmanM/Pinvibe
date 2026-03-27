from rest_framework.viewsets import ModelViewSet
from .serializer import UserSerializer, ProfileSerializer
from .models import User, Profile
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class ProfileViewset(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]

    
