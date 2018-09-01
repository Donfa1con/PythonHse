from help_function import record_to_file, read_the_file
import requests
from datetime import datetime
import json

access_token = '???'


def get_midnight():
    now = datetime.now()
    midnight =  now.replace(hour=0, minute=0, second=0, microsecond=0)
    midnight = midnight.timestamp()
    return midnight


def get_last_news(access_token):
    url = 'https://api.vk.com/method/newsfeed.search'
    midnight = get_midnight()
    params = {
            'q' : 'python',
            'count' : 200,
            'start_time' : midnight,
            'v' : 5.62,
            'extended' : True,
            'fields' : 'id',
            }
    news = json.loads(requests.get(url, params=params).text)
    return news
   

def is_suitable_news(each_news, profiles):
    big_size_of_text = 1500
    for profile in profiles:
        if each_news['owner_id'] == profile['id'] or len(each_news['text']) > big_size_of_text:
            return False
    if each_news['owner_id'] == each_news['from_id'] and each_news['text'] != '':
        if not each_news.get('attachments'):
            return False
        if each_news['attachments'][0]['type'] == 'link':
            return True
            
def get_suitable_news(news):
    news_list = []
    profiles = news['response']['profiles']
    for each_news in news['response']['items']:
        if is_suitable_news(each_news, profiles):
            each_news['text'] = each_news['text'].replace('<br>', '')
            each_news['text'] = each_news['text'].replace('&amp;quot;', '"')
            each_news['text'] = each_news['text'].replace('&amp;', '&')
            cuted_data_of_news = {
                'id' : each_news['id'],
                'owner_id' : each_news['owner_id'],
                'text' : each_news['text']
                }
            news_list.append(cuted_data_of_news)
    return news_list

def main():
    news = get_last_news(access_token)
    news_list = get_suitable_news(news)
    record_to_file(news_list, 'News.json')

if __name__ == '__main__':
    main()
