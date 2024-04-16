from mailbox import Babyl
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from .permitions import IsOwnerOrReadOnly
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.authentication import TokenAuthentication
from main.models import Setting,  Projects, Comments, AdminProject
from rest_framework_simplejwt.authentication import JWTAuthentication
from main.serializers import PostSerializer, ProjectSerializer, CommentSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny


class PostViewSet(ViewSet, ListAPIView, CreateAPIView, UpdateAPIView):
    queryset = Setting.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)


class ProjectViewSet(ViewSet, ListAPIView, CreateAPIView,
                     UpdateAPIView, RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()


class CommentViewSet(ViewSet, CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
