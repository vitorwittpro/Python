import time

def make_album(artist, album_title, number_of_songs=None):
    album = {"artist": artist, "album_title": album_title}
    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    
    return album


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


def send_messages(to_send,  sent):
    while to_send:
        current_msg = to_send.pop()
        print(current_msg)
        sent.append(current_msg)

        time.sleep(1)