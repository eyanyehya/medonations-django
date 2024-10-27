from django.http import HttpResponse
from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer

class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

def hello_world(request):
    return HttpResponse('<h1>Hello, World!</h1>')
