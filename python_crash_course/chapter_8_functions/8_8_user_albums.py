albums = []

def make_album(artist, album_title, number_of_songs=None):
    album = {"artist": artist, "album_title": album_title}
    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    
    return album

while True:
    print("\nAdd a new album")
    print("Enter 'q' to exit")

    
    artist = input("Artist: ")
    if artist == 'q': 
        break
    
    album_title = input("Album Title: ")
    if album_title == 'q': 
        break
    
    
    number_of_songs = input("Number of Songs (optional): ")
    if number_of_songs == 'q': 
        break

    new_album = make_album(artist=artist, album_title=album_title, number_of_songs=number_of_songs)
    albums.append(new_album)


print(albums)


