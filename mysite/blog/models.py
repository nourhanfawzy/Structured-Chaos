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
