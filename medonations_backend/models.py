from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subTitle = models.CharField(max_length=300)
    content = models.TextField()
    date_published = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)  # Automatically set to now when object is first created
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='blogs/', default="no-image.jpeg")  # Images will be uploaded to MEDIA_ROOT/press_releases

    def __str__(self):
        return self.title