def registerQuery(connection, email, nombre,contrasena,direccion,tarjeta):
    mycursor = connection.cursor()
    mycursor.execute("SELECT 'E_MAIL' FROM public.USUARIO")

    myresult = mycursor.fetchall()

    for x in myresult:
        
        if(email==x[0]):
            return (False,"El E-mail ya esta registrado")
    mycursor = connection.cursor()
 
    mycursor.execute('''INSERT INTO USUARIO (E_MAIL, NOMBRE, CONTRASENA, DIRECCION, TARJETA, PUNTOS) 
        VALUES ('%s', '%s', '%s', '%s', '%s', '0')'''%(email, nombre,contrasena,direccion,tarjeta))
    connection.commit()
    return (True,"Usuario registrado correctamente")

def loginUserQuery(connection, emailUser,contrasenaUser):
    mycursor = connection.cursor()
    mycursor.execute("SELECT 'E_MAIL' FROM USUARIO;")

    myresult = mycursor.fetchall()

    for x in myresult:
        if(emailUser==x[0]):
            
            mycursor = connection.cursor()
            mycursor.execute("SELECT 'CONTRASENA' FROM USUARIO WHERE E_MAIL = '"+ emailUser 
            + "';")

            myresult2 = mycursor.fetchall()

            for y in myresult2:
                if(contrasenaUser==y[0]):
                    return True
    return False 

def InfoEmpresaQuery(connection, nit):
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM EMPRESA WHERE NIT = '"+ nit + "';")
    myresult = mycursor.fetchall()
    if (len(myresult)==0):
        return (None,None,None,None,None)
    else:
        return myresult[0]

def loginAdmnQuery(connection, emailAdmn, contrasenaAdmn):
    #ToDo: Ni idea de como agregar desde el React
    mycursor = connection.cursor()
    mycursor.execute("SELECT 'E_MAIL' FROM USUARIO;")

    myresult = mycursor.fetchall()

    for x in myresult:
        if(emailAdmn==x[0]):
            
            mycursor = connection.cursor()
            mycursor.execute("SELECT 'CONTRASENA' FROM ADMINISTRADOR WHERE E_MAIL = '"+ emailAdmn + "';")

            myresult2 = mycursor.fetchall()

            for y in myresult2:
                if(contrasenaAdmn==y[0]):
                    return True
    return False 

def crearProductoQuery(connection, emailAdmn, contrasenaAdmn, idProducto, nombre, imagen, descripcion, precio,
nit, inventario, descuento):
    if(loginAdmnQuery):
        mycursor = connection.cursor()
        mycursor.execute('''INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE, IMAGEN, 
        DESCRIPCION, PRECIO, NIT_EMPRESA, INVENTARIO, DESCUENTO) VALUES (%s,%s,%s,%s,%s,%s,%s,
        %s);'''%(idProducto, nombre,imagen,descripcion,precio,nit,inventario,descuento))
        connection.commit()

        return (True, "Producto agregado")

    else:
        return (False, "Autenticaci??n Invalida")

def verListadeCompras():
    #ToDo: No pude mandar datos del React
    return True
    