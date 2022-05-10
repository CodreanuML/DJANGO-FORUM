from django import forms
from TWEET.models import Board,Topics,Posts


class Board_Form(forms.ModelForm):
	nume=forms.CharField(label='Introduceti numele ')
	descriere=forms.CharField(label='Adaugati descriere ')

	class Meta :

		model=Board
		fields=['nume','descriere']



class Topic_Form(forms.ModelForm):
	nume=forms.CharField(label='Introduceti numele ')
	descriere=forms.CharField(label='Adaugati descriere')


	class Meta :
		model=Topics
		fields=['nume','descriere']



class Post_Form(forms.ModelForm):
	nume=forms.CharField(max_length=30,label='Numele postarii')
	descriere=forms.CharField(max_length=100,label='Mesajul')


	class Meta :
		model=Posts
		fields=['nume','descriere']