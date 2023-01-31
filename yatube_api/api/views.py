from api.permissions import IsAuthorOrReadOnly
from api.serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)
from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework.filters import SearchFilter
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly
)
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


class PostViewSet(ModelViewSet):
    """Post viewset."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]
    filter_backends = (SearchFilter,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    """Group viewset."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(PostViewSet):
    """Comment viewset."""

    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('id')
        post = get_object_or_404(Post, pk=post_id)
        return serializer.save(author=self.request.user, post=post)


class FollowViewSet(PostViewSet):
    """Follow viewset."""

    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, ]
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
