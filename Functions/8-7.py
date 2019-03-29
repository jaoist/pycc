def make_album(album_title, album_artist, album_tracks = None):
    """Create a dictionary of album info, track number optional."""
    if album_tracks:
        album = {'title': album_title, 'artist': album_artist, 
        'tracks': album_tracks}
    else:
        album = {'title': album_title, 'artist': album_artist}

    return album

album = make_album('Monkey Love', 'The Bananas')
print(album)
album = make_album('Honey Trap', 'The Christopher Robin Experience')
print(album)
album = make_album('Long Time in a Dark Hole', 'Dick Hodler')
print(album)
album = make_album('69 Love Songs', 'The Magnetic Fields', 69)
print(album)