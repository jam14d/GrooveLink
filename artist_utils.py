import spotipy
from spotify_auth import get_spotify_client

sp = get_spotify_client()

def get_artist_metadata(name):
    result = sp.search(q=f'artist:{name}', type='artist', limit=1)
    items = result.get('artists', {}).get('items', [])
    if not items:
        return None, None
    artist = items[0]
    return artist['name'], {
        'id': artist['id'],
        'genres': artist['genres'],
        'popularity': artist['popularity'],
        'followers': artist['followers']['total']
    }

def find_similar_by_genre(target_name):
    _, metadata = get_artist_metadata(target_name)
    if not metadata:
        return []

    genres = metadata['genres']
    if not genres:
        return []

    genre_query = " ".join([f'genre:"{g}"' for g in genres])
    results = sp.search(q=genre_query, type='artist', limit=20)
    similar_artists = []

    for artist in results['artists']['items']:
        name = artist['name']
        if name.lower() != target_name.lower():
            similar_artists.append(name)

    return similar_artists
