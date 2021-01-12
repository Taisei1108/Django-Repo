from django.urls import path
from . import views

app_name = 'WebApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('register/director/', views.RegisterDirectorView.as_view(), name='registerdirector'), #これ追加
    path('register/movie/', views.RegisterMovieView.as_view(), name='registermovie'), #これ追加
    path('writing/log/', views.WritingLogView.as_view(), name='writinglog'), #これ追加
    path('update/log/<int:pk>/', views.UpdateLogView.as_view(), name='updatelog'), # この行を追加
    path('delete/log/<int:pk>/', views.deletelog, name='deletelog'), # この行を追加
    path('delete/movie/<int:pk>/', views.deletemovie, name='deletemovie'), # この行を追加
]
