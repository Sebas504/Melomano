def get_all_songs(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT c.id, c.titulo, c.duracion_min, c.duracion_seg, a.nombre as interprete_name FROM cancion c LEFT JOIN artista a ON c.interprete_id = a.id")
        return cursor.fetchall()

def get_song_by_id(connection, song_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, titulo, duracion_min, duracion_seg, interprete_id FROM cancion WHERE id = %s", (song_id,))
        return cursor.fetchone()

def insert_song(connection, titulo, duracion_min, duracion_seg, interprete_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO cancion (titulo, duracion_min, duracion_seg, interprete_id) VALUES (%s, %s, %s, %s)",
            (titulo, duracion_min, duracion_seg, interprete_id)
        )
        connection.commit()

def update_song(connection, song_id, titulo, duracion_min, duracion_seg, interprete_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE cancion SET titulo = %s, duracion_min = %s, duracion_seg = %s, interprete_id = %s WHERE id = %s",
            (titulo, duracion_min, duracion_seg, interprete_id, song_id)
        )
        connection.commit()

def delete_song(connection, song_id):
    with connection.cursor() as cursor:
        # Eliminar relaciones en album_cancion
        cursor.execute("DELETE FROM album_cancion WHERE cancion_id = %s", (song_id,))
        # Eliminar la canción
        cursor.execute("DELETE FROM cancion WHERE id = %s", (song_id,))
        connection.commit()
