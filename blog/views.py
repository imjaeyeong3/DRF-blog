from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def create_post(request):
    serializer = PostSerializer(data=request.data)

    if not serializer.is_valid(raise_exception=True):
        return Response({"message": "Request Body Error"}, status=status.HTTP_409_CONFLICT)
    serializer.save()
    return Response({"message": "success"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def list(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def remove_post(request):
    post1 = Post.objects.filter(id=request.user.id)
    post1.delete()
    return Response({"message": "success"}, status=status.HTTP_204_NO_CONTENT)