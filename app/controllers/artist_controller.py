from flask import Blueprint, render_template, request, redirect, url_for, current_app, session, flash
from app.models.artist_model import get_all_artists, get_artist_by_id, insert_artist, update_artist, delete_artist

artist_bp = Blueprint('artist_bp', __name__)

@artist_bp.before_request
def check_login():
    if 'user_id' not in session:
        return redirect(url_for('user_bp.login'))

@artist_bp.route('/artists')
def manage_artists():
    connection = current_app.connection
    artists = get_all_artists(connection)
    return render_template('manage_artists.html', artists=artists)

@artist_bp.route('/artists/create', methods=['GET', 'POST'])
def create_artist():
    connection = current_app.connection
    if request.method == 'POST':
        nombre = request.form['nombre']
        insert_artist(connection, nombre)
        flash('Artista creado exitosamente!', 'success')
        return redirect(url_for('artist_bp.manage_artists'))
    return render_template('create_artist.html')

@artist_bp.route('/artists/edit/<int:artist_id>', methods=['GET', 'POST'])
def edit_artist(artist_id):
    connection = current_app.connection
    artist = get_artist_by_id(connection, artist_id)

    if not artist:
        flash('Artista no encontrado.', 'danger')
        return redirect(url_for('artist_bp.manage_artists'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        update_artist(connection, artist_id, nombre)
        flash('Artista actualizado exitosamente!', 'success')
        return redirect(url_for('artist_bp.manage_artists'))
    return render_template('edit_artist.html', artist=artist)

@artist_bp.route('/artists/delete/<int:artist_id>', methods=['POST'])
def delete_artist_route(artist_id):
    connection = current_app.connection
    try:
        delete_artist(connection, artist_id)
        flash('Artista eliminado exitosamente!', 'success')
    except Exception as e:
        flash(f'Error al eliminar artista: {e}', 'danger')
    return redirect(url_for('artist_bp.manage_artists'))
