from django.db import models

# Create your models here.

class post(models.Model):
	user = models.CharField(max_length = 30)
	title = models.CharField(max_length =100)
	bodytext = models.TextField()
	timestamp = models.DateTimeField()
	category = models.CharField(max_length =100)
	def __unicode__(self):
		return self.user

class comment(models.Model):
	text = models.CharField(max_length=100)
	post = models.ForeignKey(post)
	def __unicode__(self):
		return self.text


class User(models.Model):
	name = models.CharField(max_length=256)
	email = models.CharField(max_length=256)
	username = models.CharField(max_length=256)
	password = models.CharField(max_length=256)
	cpassword = models.CharField(max_length=256)
	sex = models.CharField(max_length=256)
	def __unicode__(self):
		return self.usernames



class Postt(models.Model):
	title = models.CharField(max_length=256)
	body = models.TextField()
	category = models.TextField(default="Other")

	def __unicode__(self):
		return self.title

class Commentt(models.Model):
	post = models.ForeignKey(Postt)
	comment = models.TextField()

	def __unicode__(self):
		return self.post + ': ' + self.comment[:10]	


