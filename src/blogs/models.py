from django.db import models
from tinymce.models import HTMLField

# Create your models here.
# class Blogs(models.Model):
	#Title(charfield)
	#Body=HTMLFIELD
	#keywords(charfield)
	#genre(choicefield)
	#Likes(onetomany)
	#created_by(foreignkey (user))
	#comments
class Blogs(models.Model):
	Title	= models.CharField(max_length=200)
	Body	= HTMLField()
