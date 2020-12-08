import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository  
import repositories.artist_repository as artist_repository

artist_repository.delete_all()
album_repository.delete_all()

album_1 = Album("Mothership","No Quarter", "Rock", "Led Zepplin")
album_repository.save(album_1)

album_2 = Album("Arrival","arrival", "Pop", "ABBA")
album_repository.save(album_2)

album_3 = Album("Dark Matter", "Rabbit Hole", "Dance", "CamelPhat")
album_repository.save(album_3)

artist_1 = Artist("Led Zepplin")
artist_repository.save(artist_1)

artist_2 = Artist("ABBA")
artist_repository.save(artist_2)

artist_3 = Artist("CamelPhat")
artist_repository.save(artist_3)

