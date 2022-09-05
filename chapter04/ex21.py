file_names = [
    'song1.mp3',
    'image1.JPG',
    'image2.JPG',
    'song2.Mp3',
    'video1.mp4',
    'song3.mP3'
]

def find_song(names):
    songs=[]
    for name in names:
        test_name = name.lower()
        if test_name.endswith('.mp3'):
            songs.append(name)

    return tuple(songs)

songs = find_song(file_names)
for song in songs:
    print(song)
