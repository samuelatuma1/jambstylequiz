from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
class Image(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/%Y/%m/%d')
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	url = models.URLField()
	description = models.TextField()
	created = models.DateField(auto_now_add=True, db_index=True)
	users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)
	
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
			
		super().save(*args, **kwargs)
	
	def __str__(self):
		return self.title
