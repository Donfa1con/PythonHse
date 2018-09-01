import requests
import json
import sys

client_secret = '???'

def get_vk_user_id(user_name, client_secret):
    url = 'https://api.vk.com/method/users.get'
    params = {
            'user_ids' : user_name,
            'client_secret' : client_secret,
            'v' : 5.62
            }
    response = json.loads(requests.get(url, params=params).text)
    if response.get('response'):
        user_id = response['response'][0]['id']
        return user_id

def get_friends(user_id, client_secret):
    url = 'https://api.vk.com/method/friends.get'
    params = {
            'user_id' : user_id,
            'client_secret' : client_secret,
            'fields' : 'online',
            'v' : 5.62
            }
    response = json.loads(requests.get(url, params=params).text)
    if response.get('response'):
        list_friends_online = response['response']['items']
        return list_friends_online
    
    
def get_friends_online(list_friends):
    list_friends_online = []
    for friend in list_friends:
        if friend['online']:
            profile_url = 'https://vk.com/id%s' % friend['id']
            friend_params = {
                            'url' : profile_url,
                            'first_name' : friend['first_name'],
                            'last_name' : friend['last_name']
                            }
            list_friends_online.append(friend_params)
    return list_friends_online

def check_friends(nickname):
    if not nickname:
        return None
    user_id = get_vk_user_id(nickname, client_secret)
    if not user_id:
        return 'Invalid ID or nickname for the user'
    list_friends = get_friends(user_id, client_secret)
    if list_friends:
        list_friends_online = get_friends_online(list_friends)
        if not list_friends_online:
            list_friends_online =  'No friends online'
    elif isinstance(list_friends, list):
        list_friends_online = 'User has no friends'
    else:
           list_friends_online = 'User was deleted or banned'
    return list_friends_online

    
    
