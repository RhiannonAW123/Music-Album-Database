from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (name, title, genre, artist) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [album.name, album.title, album.genre, album.artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


def selct_all():
    albums = []

    sql = "SELECT * FROM albums"  
    results = run_sql(sql)

    for row in results:
        album = Album(row['name'], row['title'], row['genre'],row['artist'], row['id'])
        albums.append(album)
    return album

def select(id):
    album = None
    sql = "SELECT  * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0] 

    if result is not None:
        album = Album(result['name'], result['title'], result['genre'], result['artist'], result['id'])  
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(album):
    sql = "UPDATE albums SET (name, artist_id, title, genre, artist) = (%s, %s, %s, %s, %s) WHERE id  = %s"
    values  = [album.name, album.artist.id, album.title, album.genre, album.artist, album.id]
    run_sql(sql, values)



