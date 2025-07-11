def get_all_artists(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, nombre FROM artista")
        return cursor.fetchall()

def get_artist_by_id(connection, artist_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, nombre FROM artista WHERE id = %s", (artist_id,))
        return cursor.fetchone()

def insert_artist(connection, nombre):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO artista (nombre) VALUES (%s)", (nombre,))
        connection.commit()

def update_artist(connection, artist_id, nombre):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE artista SET nombre = %s WHERE id = %s", (nombre, artist_id))
        connection.commit()

def delete_artist(connection, artist_id):
    with connection.cursor() as cursor:
        # Antes de eliminar un artista, debes manejar las dependencias:
        # 1. Canciones que tienen este artista como intérprete
        # 2. Álbumes que tienen este artista en album_artista
        # Puedes optar por:
        # a) Establecer interprete_id a NULL en canciones
        # b) Eliminar las canciones asociadas
        # c) Eliminar las entradas en album_artista

        # Opción a: Establecer interprete_id a NULL en canciones
        cursor.execute("UPDATE cancion SET interprete_id = NULL WHERE interprete_id = %s", (artist_id,))
        # Opción c: Eliminar entradas en album_artista
        cursor.execute("DELETE FROM album_artista WHERE artista_id = %s", (artist_id,))

        cursor.execute("DELETE FROM artista WHERE id = %s", (artist_id,))
        connection.commit()
