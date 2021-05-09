from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	#path('login/', views.user_login, name='login'),
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('password_change/', auth_views.PasswordChangeView.as_view(), 
				name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	path('', views.dashboard, name='dashboard'),
	
	#reset password
	path('password_reset/', auth_views.PasswordResetView.as_view(),
	name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
	 name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),      name='password_reset_complete'),
	
	#Register
	path('register/', views.register, name='register'),
	
	#edit
	path('edit/', views.edit, name='edit'),
	path('myprofile', views.myprofile, name='myprofile'),
	
	#quiz
	path('quizhome/', views.quizHome, name='quizhome'),
	path('quiz/<slug:subject>/', views.quiz, name='quiz'),
	path('quizscore/', views.quizscore, name='quizscore'),
	
	path('posts/', views.posts, name='posts' ),
	path('post/', views.post, name='post')
	
]