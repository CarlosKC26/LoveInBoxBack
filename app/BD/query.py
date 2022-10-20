def register(connection, email, nombre,contrasena,direccion,tarjeta):
    mycursor = connection.cursor()
    mycursor.execute("SELECT `E_MAIL` FROM `loveinbox`.`usuario`")

    myresult = mycursor.fetchall()

    idUsuario=myresult

    for x in myresult:
        if(email==x):
            return (False,"El E-mail ya esta registrado")
    mycursor = connection.cursor()
    sql = '''INSERT INTO `loveinbox`.`usuario` (`E_MAIL`, `NOMBRE`, `CONTRASENA`, `DIRECCION`, `TARJETA`, `PUNTOS`)
        VALUES ('%s', '%s', '%s', '%s', '%s', '0');'''
    val = (email, nombre,contrasena,direccion,tarjeta)
    mycursor.execute(sql, val)
    return (True,"Usuario registrado correctamente")

def login(connection, email,contrasena):
    mycursor = connection.cursor()
    mycursor.execute("SELECT `E_MAIL` FROM `loveinbox`.`usuario`;")

    myresult = mycursor.fetchall()

    idUsuario=myresult

    for x in myresult:
        if(email==x):
            mycursor = connection.cursor()
            mycursor.execute("SELECT `CONTRASENA` FROM `loveinbox`.`usuario` WHERE `E_MAIL` = `"+ email + "`;")
            myresult = mycursor.fetchall()
            contrasenaBd=myresult
            if contrasena==contrasenaBd:
                return True
            else:
                return False

def InfoEmpresa(connection, nit):
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM `loveinbox`.`empresa` WHERE `NIT` = `"+ nit + "`;")
    myresult = mycursor.fetchall()
    return myresult
    