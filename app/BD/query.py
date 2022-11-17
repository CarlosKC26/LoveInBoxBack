def registerQuery(connection, email, nombre,contrasena,direccion,tarjeta):
    mycursor = connection.cursor()
    mycursor.execute("SELECT `E_MAIL` FROM `loveinbox`.`usuario`")

    myresult = mycursor.fetchall()

    for x in myresult:
        
        if(email==x[0]):
            return (False,"El E-mail ya esta registrado")
    mycursor = connection.cursor()
 
    mycursor.execute('''INSERT INTO `loveinbox`.`usuario` (`E_MAIL`, `NOMBRE`, `CONTRASENA`, `DIRECCION`, `TARJETA`, `PUNTOS`) 
        VALUES ('%s', '%s', '%s', '%s', '%s', '0')'''%(email, nombre,contrasena,direccion,tarjeta))
    connection.commit()
    return (True,"Usuario registrado correctamente")

def loginQuery(connection, email,contrasena):
    mycursor = connection.cursor()
    mycursor.execute("SELECT `E_MAIL` FROM `loveinbox`.`usuario`;")

    myresult = mycursor.fetchall()

    for x in myresult:
        if(email==x[0]):
            
            mycursor = connection.cursor()
            mycursor.execute("SELECT `CONTRASENA` FROM `loveinbox`.`usuario` WHERE `E_MAIL` = '"+ email + "';")

            myresult2 = mycursor.fetchall()

            for y in myresult2:
                if(contrasena==y[0]):
                    return True
    return False 

def InfoEmpresaQuery(connection, nit):
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM `loveinbox`.`empresa` WHERE `NIT` = `"+ nit + "`;")
    myresult = mycursor.fetchall()
    return myresult
    