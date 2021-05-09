from django import forms

from .models import Image

from urllib import request 
from django.core.files.base import ContentFile 
from django.utils.text import slugify

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['title', 'url', 'description']
		widgets = {
			'url': forms.HiddenInput,
			}

	def clean_url(self):
		url = self.cleaned_data['url']
		extensions = ['jpg', 'jpeg', 'png', 'svg' ]
		extension = url.rsplit('.', 1)[-1].lower()
		if extension not in extensions:
			raise forms.ValidationError('invalid extension')
		return url
		
		def save(self, force_insert=False, force_update=False, commit=True):
			image = super().save(commit=False)
			image_url = image.url
			#image_url = self.cleaned_data['url']
			name = slugify(self.title)
			extension = image_url.rsplit('.', 1)[-1].lower()
			image_name = f'{name}.{extension}'
			
			#download image via url
			response = request.urlopen(image_url)
			#add image to database
			image.image.save(image_name, ContentFile(response.read()), save=False)
			
			if commit:
				image.save()
			
			return image