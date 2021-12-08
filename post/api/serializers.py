from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from post.models import Post # If used custom user model

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # Tuple of serialized model fields (see link [2])
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(PostSerializer, self).__init__(*args, **kwargs)
