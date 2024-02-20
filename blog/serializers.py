from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer for the Blog model.

    This serializer is used to convert Blog model instances to JSON representation.

    Attributes:
        Meta (class): Specifies metadata for the serializer.

    Example Usage:
    ```
    blog_serializer = BlogSerializer(data={'title': 'Sample Post', 'content': 'This is a sample blog post.', 'Link': 'https://example.com/sample', 'cover_image': 'sample.jpg'})
    ```

    
    """
    class Meta:
        model = Blog 
        fields = '__all__' 