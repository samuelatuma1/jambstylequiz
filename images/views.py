from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
from .forms import ImageForm
from django.http import HttpResponse

# Create your views here.
@login_required
def image_create(request):
	if request.method == 'POST':
		form = ImageForm(data=request.POST)
		if form.is_valid():
			new_item = form.save(commit=False)
			new_item.user = request.user
			new_item.save()
			messages.success(request, 'Image successfully uploaded')
			
			#redirect to newly created item detail view
			return redirect(new_item.get_absolute_url())
			
	else:
		form = ImageForm(data=request.GET)
		return render(request, 'images/create.html', {
			'section': 'images',
			'form': form
		})
		
