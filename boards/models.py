from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.name
    
    def get_last_post(self):
        return Post.objects.filter(topic__board =self).order_by('-date').first()

class Topic(models.Model):
    topic = models.CharField(max_length=50)
    board = models.ForeignKey(Board,on_delete=models.CASCADE,related_name="topics")
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="topics")
    date = models.DateTimeField(auto_now_add=True)
    view = models.PositiveIntegerField(default=0)


    def __str__(self) -> str:
        return self.subject
    

class Post(models.Model):
    massage = models.TextField(max_length=5000, verbose_name='Message')
    topic  = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name="posts")
    date = models.DateTimeField(auto_now_add=True)
    edited_dt = models.DateTimeField(null=True)
    
    def __str__(self) -> str:
        return self.massage

