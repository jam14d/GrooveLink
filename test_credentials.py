from spotify_auth import get_spotify_client

sp = get_spotify_client()
artist = sp.search(q='artist:Adele', type='artist')
print(artist['artists']['items'][0]['name'])  # Should print "Adele"
