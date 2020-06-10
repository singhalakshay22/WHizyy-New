from django import forms
from tinymce.models import HTMLField

from .models import BlogPost
from .models import Comment

class BlogForm(forms.ModelForm):
	choices_ac = (
        ('FOOD', 'FOOD'),
        ('TRAVEL' , 'TRAVEL'),
        ('MUSIC','MUSIC'),
        ('FASHION','FASHION'),
        )

	# title					= models.CharField(max_length=200)
	# body					= HTMLField()
	# category				= models.CharField(choices=choices_ac, max_length=100)
	# image		 			= models.ImageField(upload_to=upload_location, null=True, blank=True)
	# date_published 			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	# date_updated 			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	# author 					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
	# slug 					= models.SlugField(blank=True, unique=True)
	# liked_by 				= models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_by')

	title = forms.CharField(required=True,label='Title',max_length=100,widget=forms.TextInput(attrs={'class': 'input--style-6'}))
	category = forms.CharField(required=True,max_length=100,widget=forms.Select(choices=choices_ac,attrs={'class': 'input--style-6'}))
	#widget=forms.Select( choices=choices_ac, attrs={'class': 'form-control' })
	image= forms.FileField(required=False,widget=forms.FileInput())
	body=HTMLField()
	class Meta:
		model = BlogPost
		fields = ['title','category','body','image']


class CommentForm(forms.ModelForm):
	body=forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'class': 'form-control form-control-pill'}))
	class Meta:
		model = Comment
		fields = ['body']