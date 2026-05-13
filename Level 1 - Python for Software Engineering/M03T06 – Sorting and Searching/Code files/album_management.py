"""
----------------------------------------------

Lillia Lessev

Abstract Data Types

----------------------------------------------

"""

print("\n--------------------------------------------------------\n")

class Album:
    
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist
    
    def __str__(self):
        new_album = Album(self.album_name, self.number_of_songs, self.album_artist)
        album_str = (f"{new_album.album_name}, {new_album.album_artist}, {new_album.number_of_songs}")
        return album_str
    
album1 = Album("Fearless", 16, "Taylor Swift")
album2 = Album("Speak Now", 14, "Taylor Swift")
album3 = Album("Red", 16, "Taylor Swift")
album4 = Album("1989", 13, "Taylor Swift")
album5 = Album("reputation", 15, "Taylor Swift")

albums1 = [album1, album2, album3, album4, album5]

# Sorting by num of songs in album
sorted_albums = sorted(albums1, key=lambda album: album.number_of_songs)

# Printing Sorted Albums
print("First list of sorted albums:\n")
for i in range(len(sorted_albums)):
    print(sorted_albums[i])

# Swapping index 0 and 1
temp_album = sorted_albums[0]
sorted_albums[0] = sorted_albums[1]
sorted_albums[1] = temp_album

# Printing Albums
print("\nSwapped index 0 and 1:\n")
for i in range(len(sorted_albums)):
    print(sorted_albums[i])

# New album list
album6 = Album("Lover", 18, "Taylor Swift")
album7 = Album("folklore", 16, "Taylor Swift")
album8 = Album("evermore", 15, "Taylor Swift")
album9 = Album("Midnights", 13, "Taylor Swift")
album10 = Album("The Tortured Poets Department: The Anthology", 31, "Taylor Swift")

albums2 = [album6, album7, album8, album9, album10]

# Printing Albums
print("\nSecond list of albums:\n")
for i in range(len(albums2)):
    print(albums2[i])

# Appending new albums
for i in range(len(albums1)):
    albums2.append(albums1[i])

album11 = Album("Dark Side of the Moon", 9, "Pink Floyd")
album12 = Album("Oops!...I Did It Again", 16, "Britney Spears")
albums2.append(album11)
albums2.append(album12)

# Printing new list
print("\nAppended list of albums:\n")
for i in range(len(albums2)):
    print(albums2[i])

# Sorting alphabetically
albums2.sort(key=lambda album: album.album_name)
#albums2 = sorted(albums2, key=lambda album: album.album_name)

# Printing Albums
print("\nAlbums sprted alphabetically by album name:\n")
for i in range(len(albums2)):
    print(albums2[i])
    
chosen_name = "Dark Side of the Moon"
for i in range(len(albums2)):
    if albums2[i].album_name == chosen_name:
        found_album = albums2[i]
        print(f"\n\n{chosen_name} is at index {i}")
        
print("\n--------------------------------------------------------\n")