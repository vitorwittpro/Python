def make_album(artist, album_title, number_of_songs=None):
    album = {"artist": artist, "album_title": album_title}
    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    
    return album

new_album = make_album('eric', 'departure')

print(new_album)

new_album = make_album('scandal', 'kudasai', 12)

print(new_album)