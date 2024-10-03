from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import Board , Topic , Post
from django.contrib.auth.models import User
from .forms import TopicForm, PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.generic import UpdateView , ListView
from django.urls import reverse_lazy
from django.utils import timezone


# Create your views here.


# def home(request):
#     boards = Board.objects.all().annotate(post_count=Count('topics__posts'))

#     x = {'boards':boards}
#     return render(request,'home.html', x )

class Home(ListView):
    model = Board
    context_object_name = 'boards'
    template_name = 'home.html'
    
    def get_queryset(self):
        
        return Board.objects.all().annotate(post_count=Count('topics__posts'))


def board(request, board_name):
    board = get_object_or_404(Board, name=board_name)

    return render(request,'board.html',{"b_id": board})

@login_required
def new_topic(request,board_name):
    board = get_object_or_404(Board, name=board_name)
    
    if request.method == 'POST':
        owner = request.user

        topic = TopicForm(request.POST)
        post = PostForm(request.POST)
        if topic.is_valid() and post.is_valid():
            
            topic= topic.save(commit=False)
            topic.board = board
            topic.owner = owner
            topic.save()

            post = post.save(commit=False)
            post.topic = topic
            post.owner = owner
            post.save()
        return redirect('board', board_name=board.name)
    else:
        topic = TopicForm()
        post = PostForm()
    return render(request,'new_topic.html',{'topic':topic,'post':post,'board':board})
    
def topic_post(request,board_name,topic_name):

    topic= get_object_or_404(Topic,board__name=board_name, topic = topic_name)
    topic.view += 1
    topic.save()
    return render(request,'topic_post.html',{'topic':topic})

@login_required
def post_reply(request, board_name,topic_name):
    topic = get_object_or_404(Topic, board__name=board_name, topic=topic_name)
    if request.method == "POST":
        post  = PostForm(request.POST)
        if post.is_valid():
            post = post.save(commit=False)
            post.topic = topic
            post.owner = request.user
            post.save()
            return redirect("topic_post", board_name=board_name, topic_name = topic_name )
    else:
        post = PostForm()

        
    return render(request, 'post_reply.html',{'topic':topic,'post':post})


class UpdatePost(UpdateView):
    model = Post
    fields = ['massage']
    pk_url_kwarg = 'post_id'
    template_name = 'post_update.html'
    context_object_name ='post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.edited_dt= timezone.now()
        post.save()

        return redirect('topic_post', board_name=post.topic.board.name, topic_name = post.topic.topic)


 











#  def new_topic(request, board_name):
#     board = get_object_or_404(Board, name=board_name)
#     owner = User.objects.first()  # Assuming you're setting the first user as the owner for testing
    
#     if request.method == 'POST':
#         topic_form = TopicForm(request.POST)
#         post_form = PostForm(request.POST)
        
#         if topic_form.is_valid() and post_form.is_valid():
#             # Save the topic but do not commit yet, as we need to set the board and owner
#             topic = topic_form.save(commit=False)
#             topic.board = board
#             topic.owner = owner  # Assuming a default user, replace with actual logged-in user
#             topic.save()

#             # Save the post and associate it with the topic and owner
#             post = post_form.save(commit=False)
#             post.topic = topic
#             post.owner = owner
#             post.save()

#             # Redirect to the board's topics after successful form submission
#             return redirect('board', board_name=board.name)
    
#     else:
#         topic_form = TopicForm()
#         post_form = PostForm()

#     return render(request, 'new_topic.html', {
#         'topic_form': topic_form,
#         'post_form': post_form,
#         'board': board
#     })

        












