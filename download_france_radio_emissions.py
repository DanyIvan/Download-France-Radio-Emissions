import requests

# Graphql service of france radio
url ='https://openapi.radiofrance.fr/v1/graphql' 

# You can obtain a token here: https://developers.radiofrance.fr
token = 'your token'
headers = {'X-Token': token}

#list of my favorite emissions
favorite_emissions = {
        'chemins_philo': '"https://www.franceculture.fr/emissions/les-chemins-de-la-philosophie"',
        'allegretto': '"https://www.francemusique.fr/emissions/allegretto"',
        'van_bethoveen': '"https://www.francemusique.fr/emissions/le-van-beethoven"',
        'methode_scientifique': '"https://www.franceculture.fr/emissions/la-methode-scientifique"',
        'open_jazz' : '"https://www.francemusique.fr/emissions/open-jazz"'
        }

def get_url_stream_show(url_show):
    """
    This function posts a graphql query to France Rdio API to get the url of
    stream of the last emition of a show
    INPUT:
        url_show (string) url of show
    OUTPUT:
        url and tile of show (tuple)
    """
    query_url_show='''
    {
    diffusionsOfShowByUrl(url:
    '''+ url_show + ''',
    first: 2) {
    edges {
    cursor
    node {
    podcastEpisode {
    url
    title
    }
    }
    }
    }
    }''' 
    r = requests.post(url, json = {'query': query_url_show}, headers = headers)
    dict_response =eval(r.text.replace('null', 'None'))
    last_emission = (dict_response['data']['diffusionsOfShowByUrl']['edges'][0]['node']['podcastEpisode']['url'])
    penultimate_emission = (dict_response['data']['diffusionsOfShowByUrl']['edges'][1]['node']['podcastEpisode']['url'])
    if last_emission:
        return last_emission
    else:
        return penultimate_emission   

def download_emissions_mp3(url_stream, show_title, save_path):
    '''
    This function downloads an mp3 from a url and saves it in a zip
    INPUT:
        url_stream(string): url of the mp3
        show_title(string): title of show
        save_path(string): path where the files are going to be saved
    '''
    url = url_stream
    r = requests.get(url)
    name_mp3 = '{}/{}.mp3'.format(save_path,show_title)
    with open(name_mp3, 'wb') as f:
        f.write(r.content)

def download_list(list_of_emissions):
    '''
    Download list of emissions
        INPUT
        list_of_emissions(list): list of names of emission from the dictionary of favorite emissions.
    '''
    save_path = 'mp3'
    for emission in list_of_emissions:
        url_stream = get_url_stream_show(favorite_emissions[emission])
        download_emissions_mp3(url_stream, emission, save_path)

if __name__ == '__main__':
    #delete_folder_contents('mp3/')    
    download_list(['allegretto',
                   'chemins_philo',
                   'methode_scientifique',
                   'van_bethoveen',
                   'open_jazz' ])
