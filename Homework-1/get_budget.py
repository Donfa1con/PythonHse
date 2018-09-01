from Function import *

print('Бюджет фильма \'Пила 2\':')
budget = make_tmdb_api_request(method='/movie/215', api_key=token)['budget']
print(budget)
