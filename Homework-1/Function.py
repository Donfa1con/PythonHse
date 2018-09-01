import urllib.request
import urllib.parse
import json
from urllib.error import HTTPError
from time import sleep
from random import shuffle

token='???'

def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)


def get_list_of_movies():
    list_of_movies=[]
    ID = 0
    while(len(list_of_movies) != 1000):
        ID += 1
        try:
            list_of_movies.append(make_tmdb_api_request(method='/movie/'+str(ID), api_key=token))
        except HTTPError as exeption:
            if exeption.code == 429:
                time.sleep(3)
            elif exeption.code == 404:
                pass
    return list_of_movies

def recommend_substring(my_movie, list_of_movies):
    recommendations=[]
    for movie in list_of_movies:
        if my_movie.lower() in movie["title"].lower():
            recommendations.append(movie["title"])
        elif my_movie.lower() in movie["original_title"].lower():
            recommendations.append(movie["original_title"])
    if len(recommendations):
        for movie in sorted(recommendations):
            print(movie)
    else:
        print("-")

def record_to_file(list_of_movies):
    with open("Data.json", "w", encoding="utf-8") as file:
        json.dump(list_of_movies, file)

        
def read_the_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def find_film(my_movie,list_of_movies):
    details = {}
    for movie in list_of_movies:
        if my_movie.lower() in [movie["title"].lower() , movie["original_title"].lower()]:
            details = movie
            break
    return details

def is_offer_same_name(details_my_movie, movie):
    if details_my_movie["title"] != movie["title"]:
            if details_my_movie["title"][0:5] in movie["title"]:
                return True
    return False

def is_offer_genre(details_my_movie, movie):
    if movie['genres'] and details_my_movie['genres']:
        if details_my_movie["genres"][0]['name']==movie["genres"][0]['name']:
            return True
    return False

def is_offer_vote(details_my_movie, movie):
    top_value = 0.5
    low_value = 0.5
    if movie["vote_average"] - low_value <= details_my_movie["vote_average"] <= movie["vote_average"] + top_value:
        return True
    return False
    
def print_recomendations(details_my_movie,list_of_movies):
    recommendations = []
    if details_my_movie:
        for movie in list_of_movies:
            if is_offer_same_name(details_my_movie, movie):
                recommendations.append(movie["title"])
                continue
            if is_offer_genre(details_my_movie, movie) and is_offer_vote(details_my_movie, movie):
                recommendations.append(movie["title"])
            
        print("Рекомендуемые фильмы:")
        shuffle(recommendations)
        for movie in recommendations[:10]:
            print(movie)
    else:
        print("Такого фильма нет. Проверьте правильность названия.")
