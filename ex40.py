#Modules, Classes and Objects

class Song(object):

    def __init__(self, lyrics): #This function runs when the class is called
        self.lyrics = lyrics

    def sing_song(self):
        for line in self.lyrics:
            print(line)

rap_song = Song(["rap lyric 1 ...", "rap lyric 2 ...", "rap lyric 3 ..."]) #Instantiating a class
metal_song = Song(["metal intro ...", "metal lyrics ...", "metal solo ..."])

rap_song.sing_song() #calling a function from the created object
metal_song.sing_song()
