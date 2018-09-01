from Function import read_the_file
from Function import find_film
from Function import print_recomendations


details_my_movie = {}
list_of_movies = []
list_of_movies = read_the_file("Data.json")

my_movie = input("Введите название фильма:\n")
details_my_movie = find_film(my_movie,list_of_movies)
print_recomendations(details_my_movie,list_of_movies)
