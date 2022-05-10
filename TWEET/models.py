from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Board(models.Model):
	nume=models.CharField(max_length=30)
	descriere=models.TextField(max_length=100)


	def __str__(self):
		return self.nume

class Topics(models.Model):
	nume=models.CharField(max_length=30)
	descriere=models.CharField(max_length=100)
	board=models.ForeignKey(Board, related_name='topics',on_delete=models.CASCADE,default=None)
	data_initiere=models.DateTimeField()
	utilizator=models.ForeignKey(User,related_name='User_Topic',on_delete=models.CASCADE,default=None)

	def __str__(self):
		return self.nume



class Posts(models.Model):
	nume=models.CharField(max_length=30)
	descriere=models.CharField(max_length=100)
	topic=models.ForeignKey(Topics, related_name='posts',on_delete=models.CASCADE,default=None)
	data_initiere=models.DateTimeField()
	aprecieri=models.IntegerField(default=0)
	utilizator=models.ForeignKey(User,related_name='User_Post',on_delete=models.CASCADE,default=None)


	def __str__(self):
		return self.nume
