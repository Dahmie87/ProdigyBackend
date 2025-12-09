from rest_framework import generics, permissions, viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer, TestSerializer, UserUpdateSerializer
from .models import Tests

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class TestView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TestSerializer

    def get_queryset(self):
        return Tests.objects.filter(student_user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student_user=self.request.user)


class UserUpdateView(GenericAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request):
        user = request.user
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
