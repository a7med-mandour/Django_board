from django import forms
from .models import Topic, Post
from django.contrib.auth.models import User




class TopicForm(forms.ModelForm):
   class Meta:
        model = Topic
        fields = ['topic']
        widgets = {
            'topic': forms.TextInput(attrs={'placeholder': 'enter the topic name'})}
        # help_texts = {
        #     'topic': 'Please enter a title for your topic.',
            
        # }

class PostForm(forms.ModelForm):
      class Meta:
        model = Post
        fields = ['massage']


