import requests
import json
from help_function import record_to_file

api_key = '???'

def load_data_from_url(method, api_key):
    headers = { 'X-Api-App-Id' : api_key }
    url = 'https://api.superjob.ru/2.0/%s' % method
    params = {
            'town' : 4,
            'count' : 100,
            'catalogues[]' : [604, 45, 47, 48, 49, 51],
            'keywords[]' : ['программист','разработчик']
    }
    data = json.loads(requests.get(url, headers=headers, params=params).text)
    return data

if __name__ == '__main__':
    data = load_data_from_url('vacancies', api_key)
    record_to_file(data['objects'],'Data.json')
