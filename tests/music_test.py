import unittest
from models.album import Album

class TestMusic(unittest.TestCase):

    def setUp(self):
        self.album = Album("Mothership", "No Quarter", "Rock", "Led Zepplin")

    def test_album_has_name(self):
        self.assertEqual("Mothership", self.album.name)
    
    def test_album_has_title(self):
        self.assertEqual("No Quarter", self.album.title)

    def test_album_has_genre(self):
        self.assertEqual("Rock", self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual("Led Zepplin", self.album.artist)

