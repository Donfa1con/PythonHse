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

def print_friends(list_friends):
    if list_friends:
        list_friends_online = get_friends_online(list_friends)
        if list_friends_online:
            for friend in list_friends_online:
                print(friend['first_name'], friend['last_name'], friend['url'])
        else:
            print('No friends online')
    elif isinstance(list_friends, list):
        print('User has no friends')
    else:
        print('User was deleted or banned')


def check_friends():
    user_id = get_vk_user_id(sys.argv[1], client_secret)
    if not user_id:
        print('Invalid ID or nickname for the user')
    else:
        list_friends = get_friends(user_id, client_secret)
        print_friends(list_friends)

        
if __name__ == '__main__':
    check_friends()

    
    
