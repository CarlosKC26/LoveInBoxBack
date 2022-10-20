from multiprocessing.connection import Connection
from flask import Flask
from datetime import datetime
import BD.bdConnection as bdConnection

connection=bdConnection.bdConnection()

app = Flask(__name__)

if __name__=="__main__":
    app.run(debug=True) #como npm start