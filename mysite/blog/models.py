from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Section(models.Model):
	section_name = models.CharField(max_length=200)
	enabled = models.BooleanField()

	def __unicode__(self):
		return self.section_name

class Post(models.Model):
	title = models.CharField(max_length=200)
	body = HTMLField()
	post_tags = models.CharField(max_length=200)
	created_on = models.DateTimeField('created on', null=True)
	section = models.ForeignKey(Section)
	author = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

	def return_tags(self):
		return self.post_tags.strip()

	return_tags.short_description = "Tags"

class Comment(models.Model):
	user_name = models.CharField(max_length=200)
	comment = models.TextField(max_length=200)
	commented_on_post = models.ForeignKey(Post)

	def __unicode__(self):
		return self.comment