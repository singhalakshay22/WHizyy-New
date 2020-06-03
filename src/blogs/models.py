from django.db import models
from tinymce.models import HTMLField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
# class Blogs(models.Model):
	#keywords(charfield)
	#genre(choicefield)
	#comments

def upload_location(instance, filename):
	file_path = 'blog/{author_id}/{title}-{filename}'.format(
				author_id=str(instance.author.id),title=str(instance.title), filename=filename)
	return file_path

class BlogPost(models.Model):
	choices_ac = (
        ('FOOD', 'FOOD'),
        ('TRAVEL' , 'TRAVEL'),
        ('MUSIC','MUSIC'),
        ('FASHION','FASHION'),
        )

	title					= models.CharField(max_length=200)
	body					= HTMLField()
	category				= models.CharField(choices=choices_ac, max_length=100)
	image		 			= models.ImageField(upload_to=upload_location, null=True, blank=True)
	date_published 			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	author 					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
	slug 					= models.SlugField(blank=True, unique=True)
	liked_by 				= models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_by')

	def __str__(self):
		return self.title

@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 

def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.author.username + "-" + instance.title)

pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)


