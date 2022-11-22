import psycopg2

def bdConnection():
    try:
        connection=psycopg2.connect(
            host='ec2-52-23-131-232.compute-1.amazonaws.com',
            port='5432',
            user='ltuttwogfqymwf',
            password='3891b123ac200faacb62b650d825541215aa3c150bf9314c4d6f3204ce474aff',
            dbname='d3f64s8qrp5ik9'
        )

        #if connection.is_connected():
        #    print("Conexión exitosa con MySQL")
        #    info_server=connection.get_server_info()
        #    print(info_server)
        #    cursor=connection.cursor()
        #    cursor.execute("SELECT DATABASE()")
        #    row=cursor.fetchone()
        #    print('Conectado a la base de datos {}'.format(row))
        return connection
    except Exception as ex:
        return print(ex)
    