from django.shortcuts import render,redirect
from .models import Board,Topics,Posts
# Create your views here.
from django.core.paginator import Paginator
from .forms import Board_Form , Topic_Form , Post_Form
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):

	boards_querry=Board.objects.all()
	pag_object=Paginator(boards_querry,5)
	page=request.GET.get('page')
	page_obj=pag_object.get_page(page)


	session_enq=request.session

	return render(request,'home.html',{'page_obj':page_obj})



@login_required
def board(request,pk):
	boards_querry=Board.objects.get(pk=pk)
	topic_querry=Topics.objects.filter(board=boards_querry)
	
	pag_object=Paginator(topic_querry,5)
	page=request.GET.get('page')
	page_obj=pag_object.get_page(page)

	return render(request, 'board.html',{'page_obj':page_obj,'board':boards_querry})



@login_required
def topic(request,pk):
	topic_querry=Topics.objects.get(pk=pk)
	post_querry=Posts.objects.filter(topic=topic_querry)
	pag_object=Paginator(post_querry,5)
	page=request.GET.get('page')
	page_obj=pag_object.get_page(page)

	
	return render(request, 'topic.html',{'page_obj':page_obj,'topic':topic_querry})



@login_required
def new_board(request):
	if request.method == "POST":
		form=Board_Form(request.POST)
		if form.is_valid() :
			board_new=form
			board_new.save()

			return redirect('TWEET:home')

	else :

		form=Board_Form()

	return render(request, 'new_board.html',{'form':form})	



@login_required
def new_topic(request,pk):
	user=request.user
	board=Board.objects.get(pk=pk)
	if request.method=="POST":
		form=Topic_Form(request.POST)
		if form.is_valid() :
			topic=form.save(commit=False)
			topic.board=board
			topic.data_initiere=datetime.now()
			topic.utilizator=user	
			topic.save()
			return redirect('TWEET:board' , pk=pk)


	else:
		form=Topic_Form()

	return render(request, 'new_topic.html',{'form':form})



@login_required
def new_post(request,pk):

	user=request.user
	topic=Topics.objects.get(pk=pk)


	if request.method=="POST":
		form=Post_Form(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.topic=topic
			post.data_initiere=datetime.now()
			post.utilizator=user
			post.save()
			return redirect('TWEET:topic',pk=pk)
	else :
		form=Post_Form()

	return render(request, 'new_post.html',{'form':form})



@login_required
def post_edit(request,pk):
	user_enq=request.user
	post=Posts.objects.get(pk=pk)


	if user_enq.username!=post.utilizator.username :
		messages.warning(request, 'You cannot edit somebodyelse posts')
		return redirect('TWEET:home')


	if request.method=="POST":
		form=Post_Form(request.POST)
		if form.is_valid():
			post.nume=form.cleaned_data['nume']	
			post.descriere=form.cleaned_data['descriere']
			post.data_initiere=datetime.now()
			post.save()
			return redirect('TWEET:topic',pk=post.topic.pk)
	else :
		form=Post_Form(initial={'nume':post.nume,'descriere':post.descriere})

	return render(request, 'edit_post.html',{'form':form})



