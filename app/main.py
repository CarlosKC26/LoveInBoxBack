from multiprocessing.connection import Connection
from flask import Flask
#from datetime import datetime
#from flask_cors import CORS
import BD.bdConnection as bdConnection
import BD.query as query

connection=bdConnection.bdConnection()

app = Flask(__name__)

if __name__=="__main__":
    app.run(debug=True) #como npm start
    #print(query.login(connection,'asado','c'))

