from django.urls import include,path

app_name="TWEET"


from . import views as TWEET_VIEWS


urlpatterns=[
	path('home/',TWEET_VIEWS.home,name='home'),
	path('newboard/',TWEET_VIEWS.new_board,name='add_board'),
	path('newtopic/<int:pk>',TWEET_VIEWS.new_topic,name='add_topic'),
	path('newpost/<int:pk>',TWEET_VIEWS.new_post,name='add_post'),
	path('board/<int:pk>',TWEET_VIEWS.board,name='board'),
	path('topic/<int:pk>',TWEET_VIEWS.topic,name='topic'),
	path('post/<int:pk>',TWEET_VIEWS.post_edit,name='post_edit'),
	
]