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