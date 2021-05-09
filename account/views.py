from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import authenticate, login 
from .forms import LoginForm,  UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .models import Profile, Subject, Question, Score
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def user_login(request):
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			username = cd['username']
			password = cd['password']
			user = authenticate(request, username=username, password=password)
			
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('logged in successfully')
				else:
					return HttpResponse('disabled account')
			else:
				return HttpResponse('invalid login')
			
	else:
		context = {'form': form}
		return render(request, 'account/login.html',  context)
	
@login_required
def dashboard(request):
	context = {'section': 'dashboard' }
	
	return render(request, 'account/dashboard.html', context)


def register(request):
	registered = False
	user_form =  UserRegistrationForm()
	if request.method == 'POST':
		user_form =  UserRegistrationForm(request.POST)
		
		
		if user_form.is_valid():
			password = user_form.cleaned_data['password']
			
			save_user = user_form.save(commit=False)
			save_user.set_password(password)
			save_user.save()
			
			Profile.objects.create(user=save_user)
			registered= True
			
			return render(request, 'account/register.html', {
					'registered': registered, 'new_user': save_user
			})
		else:
			return render(request, 'account/register.html', {
					'registered': registered, 'user_form': user_form, 'error_msg':
						 'Passwords must be at least six characters long, and be the same'
			})
	else:
		return render(request, 'account/register.html', {
					'registered': registered, 'user_form': user_form
			})
			
@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save(commit=True)
			
			messages.success(request, 'Your profile was updated successfully')
		else:
			messages.error(request, 'Error processing request. Please try again')
			
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
		
		
	
	return render(request, 'account/edit.html', {
							'user_form': user_form,
							'profile_form': profile_form
							})
	
	
#Quiz
@login_required
def quizHome(request):
	subjects = Subject.objects.all()
	return render(request, 'quiz/home.html',{'subjects': subjects, 'section': 'quiz'})
	
def quiz(request, subject):
	#return HttpResponse(f'{subject}')
	questions = Question.objects.filter(course__subject_name=subject).all().order_by('?')[:30]
	total = Question.objects.filter(course__subject_name=subject).all().count()
	subject = subject
	
	if total <= 30:
		total = total
	else: 
		total = 30
  
	paginator = Paginator(questions, 1)
	page = request.GET.get('page')
	try:
		quiz_questions = paginator.page(page)
	except PageNotAnInteger:
		quiz_questions = paginator.page(1)

	except EmptyPage:
		quiz_questions = paginator.page(paginator.num_pages)
  
	
	return render(request, 'quiz/quiz.html',{'subject': subject, 'section': 'quiz',
								'total': total, 'quiz_questions': quiz_questions, 'page': page})

@login_required
def quizscore(request):
	if request.method == 'POST':
		user = request.user
		subject = request.POST['subject']
		score = request.POST['scored']
		
		Score.objects.create(user=user, subject=subject, score=score)
		
		return render(request, 'quiz/quizscore.html', {'user': request.user.username, 'subject': subject, 'score': score})

@login_required		
def myprofile(request):
	return render(request, 'account/myprofile.html')
#End of quiz section

def posts(request):
	if request.method == 'POST':
		value = request.POST['value']
		new_val = f'{value} now'
		return JsonResponse({'val': new_val })
	return render(request, 'account/posts.html')
	
def post(request):
	value = request.GET.get('post')
	return JsonResponse({'value': f'{value} totos for you this night'})