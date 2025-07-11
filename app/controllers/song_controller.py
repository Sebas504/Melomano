from flask import Blueprint, render_template, request, redirect, url_for, current_app, session, flash
from app.models.song_model import get_all_songs, get_song_by_id, insert_song, update_song, delete_song
from app.models.artist_model import get_all_artists # Para el dropdown de artistas

song_bp = Blueprint('song_bp', __name__)

@song_bp.before_request
def check_login():
    if 'user_id' not in session:
        return redirect(url_for('user_bp.login'))

@song_bp.route('/songs')
def manage_songs():
    connection = current_app.connection
    songs = get_all_songs(connection)
    return render_template('manage_songs.html', songs=songs)

@song_bp.route('/songs/create', methods=['GET', 'POST'])
def create_song():
    connection = current_app.connection
    artists = get_all_artists(connection) # Obtener todos los artistas para el dropdown

    if request.method == 'POST':
        titulo = request.form['titulo']
        duracion_min = request.form['duracion_min']
        duracion_seg = request.form['duracion_seg']
        interprete_id = request.form['interprete_id'] if request.form['interprete_id'] else None

        insert_song(connection, titulo, duracion_min, duracion_seg, interprete_id)
        flash('Canción creada exitosamente!', 'success')
        return redirect(url_for('song_bp.manage_songs'))
    return render_template('create_song.html', artists=artists)

@song_bp.route('/songs/edit/<int:song_id>', methods=['GET', 'POST'])
def edit_song(song_id):
    connection = current_app.connection
    song = get_song_by_id(connection, song_id)
    artists = get_all_artists(connection)

    if not song:
        flash('Canción no encontrada.', 'danger')
        return redirect(url_for('song_bp.manage_songs'))

    if request.method == 'POST':
        titulo = request.form['titulo']
        duracion_min = request.form['duracion_min']
        duracion_seg = request.form['duracion_seg']
        interprete_id = request.form['interprete_id'] if request.form['interprete_id'] else None

        update_song(connection, song_id, titulo, duracion_min, duracion_seg, interprete_id)
        flash('Canción actualizada exitosamente!', 'success')
        return redirect(url_for('song_bp.manage_songs'))
    return render_template('edit_song.html', song=song, artists=artists)

@song_bp.route('/songs/delete/<int:song_id>', methods=['POST'])
def delete_song_route(song_id):
    connection = current_app.connection
    delete_song(connection, song_id)
    flash('Canción eliminada exitosamente!', 'success')
    return redirect(url_for('song_bp.manage_songs'))
