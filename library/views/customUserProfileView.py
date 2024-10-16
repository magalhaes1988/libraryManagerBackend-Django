from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from library.models import CustomUserProfile
from library.serializers import CustomUserProfileSerializer
from library.permissions import IsOwnerOrStaff, IsStaffOrDeny


class CustomUserProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomUserProfile.objects.all()
    serializer_class = CustomUserProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list','create','destroy']:
            self.permission_classes.append(IsStaffOrDeny)
        else:
            self.permission_classes.append(IsOwnerOrStaff)
        return [permission() for permission in self.permission_classes]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context