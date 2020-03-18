from django.db import models
from django.conf import settings
from django.urls.base import reverse

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog",  null=True)
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/blog')
    content = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
    
    
        
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey('blog', on_delete=models.CASCADE)    
    

class SendMessage(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
    

    
    