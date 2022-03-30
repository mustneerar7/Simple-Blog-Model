from rest_framework import serializers
from .models import Post

class PostSerialier(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body', 'time')