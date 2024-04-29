from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Letter, UserLearning

from .serializers import LetterSerializer, UserLearningSerializer


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    permission_classes = [AllowAny]

class UserLearningViewSet(viewsets.ModelViewSet):
    queryset = UserLearning.objects.all()
    serializer_class = UserLearningSerializer
    permission_classes = [AllowAny]