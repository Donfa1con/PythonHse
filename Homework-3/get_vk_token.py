import webbrowser

def get_vk_token():
    url = 'https://oauth.vk.com/authorize'
    redirect_uri = 'redirect_uri=https://oauth.vk.com/blank.html'
    version = 'v=5.62'
    response_type = 'response_type=token'
    main_parameters = '%s&%s&%s' % (redirect_uri, version, response_type)
    secondary_parameters = 'client_id=5899176&display=page&scope=offline'
    parameters_url = '%s&%s' % (main_parameters, secondary_parameters)
    webbrowser.open('%s?%s' % (url, parameters_url))

if __name__ == '__main__':
    get_vk_token()
