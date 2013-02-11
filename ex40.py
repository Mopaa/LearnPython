class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	def add_farts(self):
		for line in self.lyrics:
			print line+" *fart*"

happy_bday = Song(["Happy Birthday to you",
					"I don't want to get sued",
					"So i'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.add_farts()
bulls_on_parade.sing_me_a_song()