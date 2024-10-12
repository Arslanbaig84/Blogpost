from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Post(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)
    article = models.TextField(max_length=2000)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='post')
    
    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)