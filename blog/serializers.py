from rest_framework import serializers
from blog.models import Post
from django.db import models
from django.db.models import TextField


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'