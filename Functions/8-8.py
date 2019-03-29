def make_album(album_title, album_artist, album_tracks = None):
    """Create a dictionary of album info, track number optional."""
    if album_tracks:
        album = {'title': album_title, 'artist': album_artist, 
        'tracks': album_tracks}
    else:
        album = {'title': album_title, 'artist': album_artist}

    return album

#Start input loop.
while True:
    print("\nPlease describe the album: ")
    print("(enter 'q' at any time to quit)")
    
    album_title = input("Enter the title: ")
    if album_title == 'q':
        break
    
    album_artist = input("Enter the artist: ")
    if album_artist == 'q':
        break
    
    album_tracks = input("Enter the number of tracks: ")
    if album_tracks == 'q':
        break
    #Stop the loop here.
    break

    
album = make_album(album_title, album_artist, album_tracks)
print(album)