from rest_framework import serializers
from .models import blog,blog_likes,blog_comments


class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model=blog
        fields='__all__'

class likeSerializer(serializers.ModelSerializer):
    class Meta:
        model=blog_likes
        fields='__all__'

class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model=blog_comments
        fields='__all__'

