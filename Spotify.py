import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials
#import config
import os
from pprint import pprint
from dotenv import load_dotenv





def get_song(search_str):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ['client_id'],client_secret=os.environ['client_secret']))
    y = []

    data = {'name': [], 'image': []}
    
    result = sp.search(search_str,limit=30)
    result = result['tracks']['items']

    #pprint.pprint(result) -> pretty print

    for x in result:
        data['name'].append(x.get('name'))
        data['image'].append(x.get('album').get('images')[0].get("url"))


    return data





def get_popular_song(search_str):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ['client_id'],client_secret=os.environ['client_secret']))
   


    list = []

    if search_str.lower()=='random':

        randomsongs = ['central cee','dave','omah lay', 'uk rap', 'afro beats', 'bnxn', 'wizkid', 'Burnaboy']
        random_item = random.choice(randomsongs)
        
        result = sp.search(random_item, limit=50)
        result = result['tracks']['items']

        for x in result:
            data = {'name': x.get('name'), 'image': x.get('album').get('images')[0].get("url"), "popularity":x.get('popularity'), 'url': x.get('album').get('external_urls').get('spotify'),'preview': x.get('preview_url')}
            list.append(data)

        #print(list)

        ordered_list = sorted(list, key= lambda i:i['popularity'],reverse=True)
    else: 
        result = sp.search(search_str, limit=50)
        result = result['tracks']['items']
        

        for x in result:
            data = {'name': x.get('name'), 'image': x.get('album').get('images')[0].get("url"), "popularity":x.get('popularity'), 'url': x.get('album').get('external_urls').get('spotify'),'preview': x.get('preview_url')}
            list.append(data)

       
        ordered_list = sorted(list, key= lambda i:i['popularity'],reverse=True)



    return ordered_list

def get_least_popular_song(search_str):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ['client_id'],client_secret=os.environ['client_secret']))

    list = []
    if search_str.lower()=='random':

        randomsongs = ['central cee','dave','omah lay', 'uk rap', 'afro beats', 'bnxn', 'wizkid', 'Burnaboy']
        random_item = random.choice(randomsongs)
        
        result = sp.search(random_item, limit=50)
        result = result['tracks']['items']

        for x in result:
            data = {'name': x.get('name'), 'image': x.get('album').get('images')[0].get("url"), "popularity":x.get('popularity'), 'url': x.get('album').get('external_urls').get('spotify'),'preview': x.get('preview_url')}
            list.append(data)

        #print(list)

        ordered_list = sorted(list, key= lambda i:i['popularity'])
    else: 
        result = sp.search(search_str, limit=50)
        result = result['tracks']['items']

        for x in result:
            data = {'name': x.get('name'), 'image': x.get('album').get('images')[0].get("url"), "popularity":x.get('popularity'), 'url': x.get('album').get('external_urls').get('spotify'),'preview': x.get('preview_url')}
            list.append(data)

        
        ordered_list = sorted(list, key= lambda i:i['popularity'])

        return ordered_list

