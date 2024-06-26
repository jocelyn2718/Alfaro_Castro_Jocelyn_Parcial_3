# Instalaremos unas nueva libreria llamada "python-dotenv"
# que nos oermite cargar muy fácilmente los archivos 
# de variables de entorno 

# Continuamos con el modulo requests 

from dotenv import load_dotenv
import os
import base64
from requests import post,  get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# print(client_id,client_secret)
# Validar que contamos con los ID y son consultables

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_headers(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_headers(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]    
    
    if len(json_result) == 0:
        print("No artist found")
        return None
    
    return json_result[0]

#print(json_result)

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_headers(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

def main():
    artist_name = input("Ingrese el nombre del artista: ")
    token = get_token()
    result = search_for_artist(token, artist_name)

    if result:
        artist_id = result["id"]
        songs = get_songs_by_artist(token, artist_id)

        print(f"Top Tracks by Spotify de {artist_name}:")
        for idx, song in enumerate(songs):
            print(f"{idx + 1}. {song['name']}")
    else:
        print("No se encontró ningún artista con ese nombre.")

if __name__ == "__main__":
    main()

# token = get_token()
# result = search_for_artist(token, "artist name")
# artist_id = result["id"]
# songs = get_songs_by_artist(token, artist_id)

# for idx, song in enumerate(songs):
#   print(f"{idx +1}. {song['name']}")

#print(songs)
#print(result["name"])
#print(token)
