from django.http import HttpResponse
from django.shortcuts import render
from webWizard.SimpleWebSocketServer import HTTPRequest
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import User, Project, ProjectMember, Task, Comment
from .serializers import UserSerializer, ProjectSerializer, ProjectMemberSerializer, TaskSerializer, CommentSerializer


def home(request):
    return HttpResponse('Welcome')


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectMemberViewSet(ModelViewSet):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
