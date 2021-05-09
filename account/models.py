from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,
																on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
	
	def __str__(self):
		return f" Profile for user {self.user.username} "
		
# Quiz models
class Subject(models.Model):
	subject_name = models.SlugField(max_length=40)
	def __str__(self):
		return f'{self.subject_name}'
	
class Question(models.Model):
	image = models.ImageField(upload_to='questions/', blank=True)
	course = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='questions')
	question = models.CharField(max_length=300)
	optionA = models.CharField(max_length=250)
	optionB = models.CharField(max_length=250)
	optionC = models.CharField(max_length=250)
	optionD = models.CharField(max_length=250)
	options = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]
	answer = models.CharField(max_length=250, choices=options)
	
	def __str__(self):
		return self.question
	
class Score(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='scores')
	subject=models.CharField(max_length=100)
	score=models.CharField(max_length=50)
	submitted = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering= ['-submitted']
		
	def __str__(self):
		return f'{self.subject}, {self.score} on {self.submitted}'
	

#end of quiz models