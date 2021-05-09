from django.contrib import admin
from .models import Profile, Subject, Question, Score

# Register your models here.
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
	list_display = ['user', 'date_of_birth', 'photo']
	
#Quiz admin
admin.site.register(Subject)

admin.site.register(Question)

@admin.register(Score)
class registerScore(admin.ModelAdmin):
	list_display = ['subject', 'score']
#end of Quiz admin