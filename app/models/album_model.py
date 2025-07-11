def get_all_albums(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT a.id, a.titulo, a.año, a.descripcion, a.medio, u.name as usuario_name FROM album a LEFT JOIN usuarios u ON a.usuario_id = u.id")
        return cursor.fetchall()

def get_album_by_id(connection, album_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT a.id, a.titulo, a.año, a.descripcion, a.medio, a.usuario_id, u.name as usuario_name FROM album a LEFT JOIN usuarios u ON a.usuario_id = u.id WHERE a.id = %s", (album_id,))
        return cursor.fetchone()

def insert_album(connection, titulo, año, descripcion, medio, usuario_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO album (titulo, año, descripcion, medio, usuario_id) VALUES (%s, %s, %s, %s, %s)",
            (titulo, año, descripcion, medio, usuario_id)
        )
        connection.commit()

def update_album(connection, album_id, titulo, año, descripcion, medio, usuario_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE album SET titulo = %s, año = %s, descripcion = %s, medio = %s, usuario_id = %s WHERE id = %s",
            (titulo, año, descripcion, medio, usuario_id, album_id)
        )
        connection.commit()

def delete_album(connection, album_id):
    with connection.cursor() as cursor:
        # Eliminar relaciones en album_artista
        cursor.execute("DELETE FROM album_artista WHERE album_id = %s", (album_id,))
        # Eliminar relaciones en album_cancion
        cursor.execute("DELETE FROM album_cancion WHERE album_id = %s", (album_id,))
        # Eliminar el álbum
        cursor.execute("DELETE FROM album WHERE id = %s", (album_id,))
        connection.commit()

def get_album_artists(connection, album_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT ar.id, ar.nombre FROM artista ar JOIN album_artista aa ON ar.id = aa.artista_id WHERE aa.album_id = %s", (album_id,))
        return cursor.fetchall()

def add_artist_to_album(connection, album_id, artista_id):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO album_artista (album_id, artista_id) VALUES (%s, %s)", (album_id, artista_id))
        connection.commit()

def remove_artist_from_album(connection, album_id, artista_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM album_artista WHERE album_id = %s AND artista_id = %s", (album_id, artista_id))
        connection.commit()

def get_album_songs(connection, album_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT c.id, c.titulo, c.duracion_min, c.duracion_seg, ar.nombre as interprete_name FROM cancion c JOIN album_cancion ac ON c.id = ac.cancion_id LEFT JOIN artista ar ON c.interprete_id = ar.id WHERE ac.album_id = %s", (album_id,))
        return cursor.fetchall()

def add_song_to_album(connection, album_id, cancion_id):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO album_cancion (album_id, cancion_id) VALUES (%s, %s)", (album_id, cancion_id))
        connection.commit()

def remove_song_from_album(connection, album_id, cancion_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM album_cancion WHERE album_id = %s AND cancion_id = %s", (album_id, cancion_id))
        connection.commit()
