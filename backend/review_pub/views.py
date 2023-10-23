from rest_framework import viewsets

from .models import Domain, Language, Paper, Review, User
from .serializers import DomainSerializer, LanguageSerializer, PaperSerializer, ReviewSerializer, UserSerializer


class DomainViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class PaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
