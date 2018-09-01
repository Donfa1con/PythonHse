from Function import read_the_file
from Function import recommend_substring

my_movie=input("Введите название фильма:\n")
list_of_movies=read_the_file("Data.json")
print("Найденные фильмы:")
recommend_substring(my_movie, list_of_movies)
