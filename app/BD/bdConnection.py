import mysql.connector

def bdConnection():
    try:
        connection=mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='UwU:V*7HO5m4o80Ol@CvXD',
            db='loveinbox'
        )

        if connection.is_connected():
            print("Conexión exitosa con MySQL")
            info_server=connection.get_server_info()
            print(info_server)
            cursor=connection.cursor()
            cursor.execute("SELECT DATABASE()")
            row=cursor.fetchone()
            print('Conectado a la base de datos {}'.format(row))
            return connection
    except Exception as ex:
        return print(ex)
    