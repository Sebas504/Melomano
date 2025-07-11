from flask import Blueprint, render_template, request, redirect, url_for, current_app, session, flash
from app.models.album_model import (
    get_all_albums, get_album_by_id, insert_album, update_album, delete_album,
    get_album_artists, add_artist_to_album, remove_artist_from_album,
    get_album_songs, add_song_to_album, remove_song_from_album
)
from app.models.user_model import get_all_user # Para el dropdown de usuario_id
from app.models.artist_model import get_all_artists, get_artist_by_id # Para el dropdown de artistas
from app.models.song_model import get_all_songs # Para el dropdown de canciones

album_bp = Blueprint('album_bp', __name__)

@album_bp.before_request
def check_login():
    if 'user_id' not in session:
        return redirect(url_for('user_bp.login'))

@album_bp.route('/albums')
def manage_albums():
    connection = current_app.connection
    albums = get_all_albums(connection)
    return render_template('manage_albums.html', albums=albums)

@album_bp.route('/albums/create', methods=['GET', 'POST'])
def create_album():
    connection = current_app.connection
    users = get_all_user(connection) # Obtener todos los usuarios para el dropdown

    if request.method == 'POST':
        titulo = request.form['titulo']
        año = request.form['año']
        descripcion = request.form['descripcion']
        medio = request.form['medio']
        usuario_id = request.form['usuario_id']

        insert_album(connection, titulo, año, descripcion, medio, usuario_id)
        flash('Álbum creado exitosamente!', 'success')
        return redirect(url_for('album_bp.manage_albums'))
    return render_template('create_album.html', users=users)

@album_bp.route('/albums/edit/<int:album_id>', methods=['GET', 'POST'])
def edit_album(album_id):
    connection = current_app.connection
    album = get_album_by_id(connection, album_id)
    users = get_all_user(connection)

    if not album:
        flash('Álbum no encontrado.', 'danger')
        return redirect(url_for('album_bp.manage_albums'))

    if request.method == 'POST':
        titulo = request.form['titulo']
        año = request.form['año']
        descripcion = request.form['descripcion']
        medio = request.form['medio']
        usuario_id = request.form['usuario_id']

        update_album(connection, album_id, titulo, año, descripcion, medio, usuario_id)
        flash('Álbum actualizado exitosamente!', 'success')
        return redirect(url_for('album_bp.manage_albums'))
    return render_template('edit_album.html', album=album, users=users)

@album_bp.route('/albums/delete/<int:album_id>', methods=['POST'])
def delete_album_route(album_id):
    connection = current_app.connection
    delete_album(connection, album_id)
    flash('Álbum eliminado exitosamente!', 'success')
    return redirect(url_for('album_bp.manage_albums'))

@album_bp.route('/albums/<int:album_id>/details')
def album_details(album_id):
    connection = current_app.connection
    album = get_album_by_id(connection, album_id)
    if not album:
        flash('Álbum no encontrado.', 'danger')
        return redirect(url_for('album_bp.manage_albums'))

    artists = get_album_artists(connection, album_id)
    songs = get_album_songs(connection, album_id)
    all_artists = get_all_artists(connection)
    all_songs = get_all_songs(connection)

    return render_template('album_details.html', album=album, artists=artists, songs=songs, all_artists=all_artists, all_songs=all_songs)

@album_bp.route('/albums/<int:album_id>/add_artist', methods=['POST'])
def add_artist_to_album_route(album_id):
    connection = current_app.connection
    artista_id = request.form['artista_id']
    add_artist_to_album(connection, album_id, artista_id)
    flash('Artista añadido al álbum exitosamente!', 'success')
    return redirect(url_for('album_bp.album_details', album_id=album_id))

@album_bp.route('/albums/<int:album_id>/remove_artist/<int:artista_id>', methods=['POST'])
def remove_artist_from_album_route(album_id, artista_id):
    connection = current_app.connection
    remove_artist_from_album(connection, album_id, artista_id)
    flash('Artista eliminado del álbum exitosamente!', 'success')
    return redirect(url_for('album_bp.album_details', album_id=album_id))

@album_bp.route('/albums/<int:album_id>/add_song', methods=['POST'])
def add_song_to_album_route(album_id):
    connection = current_app.connection
    cancion_id = request.form['cancion_id']
    add_song_to_album(connection, album_id, cancion_id)
    flash('Canción añadida al álbum exitosamente!', 'success')
    return redirect(url_for('album_bp.album_details', album_id=album_id))

@album_bp.route('/albums/<int:album_id>/remove_song/<int:cancion_id>', methods=['POST'])
def remove_song_from_album_route(album_id, cancion_id):
    connection = current_app.connection
    remove_song_from_album(connection, album_id, cancion_id)
    flash('Canción eliminada del álbum exitosamente!', 'success')
    return redirect(url_for('album_bp.album_details', album_id=album_id))
