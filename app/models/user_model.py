# app/models/user_model.py

def get_all_user(connection):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, apellido FROM usuarios")
            return cursor.fetchall()

def get_user_by_email(connection, email):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, password FROM usuarios WHERE email=%s", (email,))
        return cursor.fetchone()

def get_user_by_id(connection, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name, apellido, email FROM usuarios WHERE id=%s", (user_id,))
        return cursor.fetchone()

def insert_user(connection, name, apellido, email, hashed_password):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO usuarios (name, apellido, email, password) VALUES (%s, %s, %s, %s)",
            (name, apellido, email, hashed_password)
        )
        connection.commit()

def get_user_basic_profile(connection, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name, apellido, email FROM usuarios WHERE id=%s", (user_id,))
        return cursor.fetchone()