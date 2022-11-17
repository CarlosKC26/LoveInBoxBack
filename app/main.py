from multiprocessing.connection import Connection
from flask import Flask,jsonify
#from datetime import datetime
#from flask_cors import CORS
import BD.bdConnection as bdConnection
import BD.query as query

connection=bdConnection.bdConnection()
#print(query.register(connection,'cgalvis@unal.edu.co','abc','1234567','cr2','4536456'))

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return jsonify({'LoveInBox esta funcionando!': True})

@app.route('/register/<email>/<nombre>/<contrasena>/<direccion>/<tarjeta>', methods = ['POST'])
def register(email, nombre,contrasena,direccion,tarjeta):
    ret=query.registerQuery(connection, email, nombre,contrasena,direccion,tarjeta)
    return jsonify({'Estado': ret[0],
    'Detalles': ret[1]})

@app.route('/login/<email>/<contrasena>', methods = ['POST'])
def login(email,contrasena):
    ret=query.loginQuery(connection, email,contrasena)
    return jsonify({'Login': ret})

#@app.route('/infoEmpresa/<email>/<contrasena>', methods = ['POST'])

if __name__=="__main__":
    app.run(debug=True) #como npm startgit 
    

