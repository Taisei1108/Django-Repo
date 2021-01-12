from django.views import generic
from WebApp.models import Movie, Director, Log
from WebApp.form import DirectorForm, MovieForm, LogForm
from django.urls import reverse
from django.shortcuts import render

#Classベースの書き方とfunctionベースの書き方の両方がある。

"""
class IndexView(generic.ListView):
    template_name = 'WebApp/index.html'
    context_object_name = 'movie_list'
    queryset = Movie.objects.all()
"""
def index(request):
    movie_list = Movie.objects.all()
    return render(request, 'WebApp/index.html', {'movie_list': movie_list})

class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'WebApp/detail.html'

class RegisterDirectorView(generic.CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'WebApp/register.html'
    def get_success_url(self):
        return reverse('WebApp:registermovie') 

class RegisterMovieView(generic.CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'WebApp/register.html'
    def get_success_url(self):
        return reverse('WebApp:movie_detail', kwargs={'pk': self.object.pk }) 

class WritingLogView(generic.CreateView):
    model = Log
    form_class = LogForm
    template_name = 'WebApp/register.html'
    def get_success_url(self):
        return reverse('WebApp:movie_detail', kwargs={'pk': self.object.movie.pk }) 

class UpdateLogView(generic.UpdateView):
    model = Log
    form_class = LogForm
    template_name = "WebApp/register.html"
    def get_success_url(self):
        return reverse('WebApp:movie_detail', kwargs={'pk': self.object.movie.pk })

class DeleteLogView(generic.DeleteView):
    model = Log
    def get_success_url(self):
        return reverse('WebApp:movie_detail', kwargs={'pk': self.object.movie.pk })

