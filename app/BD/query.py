def register(connection, email, nombre,contrasena,direccion,tarjeta):
    mycursor = connection.cursor()
    mycursor.execute("SELECT `E_MAIL` FROM `loveinbox`.`usuario`")

    myresult = mycursor.fetchall()

    idUsuario=myresult

    for x in myresult[0]:
        if(email==x):
            return (False,"El E-mail ya esta registrado")
    mycursor = connection.cursor()
    print("si llegue")
    mycursor.execute('''INSERT INTO `loveinbox`.`usuario` (`E_MAIL`, `NOMBRE`, `CONTRASENA`, `DIRECCION`, `TARJETA`, `PUNTOS`) 
        VALUES ('%s', '%s', '%s', '%s', '%s', '0')'''%(email, nombre,contrasena,direccion,tarjeta))
    connection.commit()
    return (True,"Usuario registrado correctamente")

def login(connection, email,contrasena):
    mycursor = connection.cursor()
    mycursor.execute("SELECT `E_MAIL` FROM `loveinbox`.`usuario`;")

    myresult = mycursor.fetchall()

    print(myresult)

def InfoEmpresa(connection, nit):
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM `loveinbox`.`empresa` WHERE `NIT` = `"+ nit + "`;")
    myresult = mycursor.fetchall()
    return myresult
    