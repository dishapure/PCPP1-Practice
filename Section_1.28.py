import copy

class Song:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Song({self.title!r})"

class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def __repr__(self):
        return f"Playlist({self.name!r}, {self.songs})"

# Original playlist
original = Playlist("My Mix", [Song("Imagine"), Song("Thunder")])

# Shallow copy
shallow = copy.copy(original)

# Deep copy
deep = copy.deepcopy(original)

# Check IDs
print("Playlist IDs:")
print("Original ID:", id(original))
print("Shallow  ID:", id(shallow))
print("Deep     ID:", id(deep))

print("\nSong object IDs:")
print("Original Song[0] ID:", id(original.songs[0]))
print("Shallow  Song[0] ID:", id(shallow.songs[0]))
print("Deep     Song[0] ID:", id(deep.songs[0]))
