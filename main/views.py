from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, MpaaRating
from .forms import MovieForm
import json

# Created at 16-02-2024 13:26
# Created By Harianto
# To Complete Coding Skill Test from Omni App Solutions

# Retrieve Movie List from Model
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movies': movies})

# Retrieve Detail/Specific Movie List from Model by Primary Key
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie/movie_detail.html', {'movie': movie})

# Create Page & Store Movie based on request Method (Post/Get)
def movie_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'movie/movie_form.html', {'form': form})

# Edit Movie Page & Save updated Movie based on request Method (Post/Get)
def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie/movie_form.html', {'form': form})

# Delete Movie by primary Key
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movie/movie_confirm_delete.html', {'movie': movie})

# Import Movie by JSON Files, Just Edit json_file_path)
def import_movies_from_json(request, json_file_path):
    json_file_path = 'C:\laragon\pyproject\LearnJango\movieapp\database\movies.json'
    with open(json_file_path, 'r') as file:
        movies_data = json.load(file)
        for movie_data in movies_data:
            mpaa_rating_data = movie_data.get('mpaaRating')
            mpaa_rating, _ = MpaaRating.objects.get_or_create(type=mpaa_rating_data['type'], label=mpaa_rating_data['label'])

            movie = Movie(
                id=movie_data['id'],
                name=movie_data['name'],
                description=movie_data['description'],
                imgPath=movie_data['imgPath'],
                duration=movie_data['duration'],
                genre=movie_data['genre'],
                language=movie_data['language'],
                mpaaRating=mpaa_rating,
                userRating=movie_data['userRating']
            )
            movie.save()
            
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movies': movies})