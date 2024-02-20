from django.db import models


class Blog(models.Model):
    """
    Model representing a Blog post.

    Attributes:
        title (CharField): The title of the blog post, with a maximum length of 100 characters.
        content (TextField): The content of the blog post, with a maximum length of 100 characters.
        Link (URLField): The URL associated with the blog post, with a maximum length of 200 characters.
        cover_image (ImageField): An optional field for uploading a cover image for the blog post.
    
    Methods:
        __str__(): Returns a human-readable string representation of the blog post.

    Example Usage:
    ```
    blog_post = Blog(title="Sample Post", content="This is a sample blog post.", Link="https://example.com/sample", cover_image="sample.jpg")
    ```

    Note: Adjust the attributes and methods as per your specific requirements.
    """
    title=models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    Link=models.URLField(max_length=200)
    cover_image = models.ImageField(upload_to='img', blank=True, null=True)
    
    def __str__(self):
        return self.title
    