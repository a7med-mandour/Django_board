from django.urls import path
from . import views



urlpatterns = [
    path("",views.Home.as_view(), name='home'),
    path('boards/<board_name>',views.board, name='board'),
    path('boards/<board_name>/new',views.new_topic, name='new_topic'),
    path('boards/<board_name>/<topic_name>/',views.topic_post, name= 'topic_post'),
    path('boards/<board_name>/<topic_name>/reply',views.post_reply, name= 'post_reply'),
    path('boards/<board_name>/<topic_name>/<post_id>/edit/',views.UpdatePost.as_view(), name= 'update_post'),

]



