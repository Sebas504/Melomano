# app/__init__.py
from flask import Flask
import pymysql.cursors
from config import Config

#from app.config import Config  # Asegúrate que 'config.py' esté dentro de /app
import os

def create_app():
    app = Flask(__name__)
    
    # Cargar configuración desde el archivo .env a través de config.py
    app.config.from_object(Config)

    # Conexión a la base de datos MySQL (sin ORM)
    connection = pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )

    # Guardar conexión como atributo de la app
    app.connection = connection

    # Registrar Blueprints
    from app.controllers.main_controller import main_bp
    from app.controllers.user_controller import user_bp
    from app.controllers.album_controller import album_bp
    from app.controllers.song_controller import song_bp
    from app.controllers.artist_controller import artist_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(album_bp) 
    app.register_blueprint(song_bp) 
    app.register_blueprint(artist_bp)

    return app