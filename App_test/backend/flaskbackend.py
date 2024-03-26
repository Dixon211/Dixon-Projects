from flask import Flask, jsonify, g, request
import pymssql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

serverinfo = {"server":"DESKTOP-D0OINMR", "user": "Test1", "password":"Password123!", "database":"machine_info"}


@app.before_request
def set_global():
    g.serverinfo = serverinfo

#the route will execute whatever function is under it for the specified route
@app.route("/mdata")
def servedata():
    server = g.serverinfo["server"]
    user= g.serverinfo["user"]
    password = g.serverinfo["password"]
    database= g.serverinfo["database"]

    db = pymssql.connect(
        server=server,user=user,
        password=password,
        database=database,
        as_dict=True)
    cursor=db.cursor()
    cursor.execute(f"SELECT * FROM Machine")
    rows = cursor.fetchall()
    db.close()

    return jsonify(rows)

#this route is for adding or updating the table data
@app.route("/newdata", methods=['GET','PUT', 'POST', 'DELETE'])
def newdata():
    try:
        
        #receive data
        recieved = request.json

        #connect to server
        server = g.serverinfo["server"]
        user= g.serverinfo["user"]
        password = g.serverinfo["password"]
        database= g.serverinfo["database"]

        db = pymssql.connect(
            server=server,
            user=user,
            password=password,
            database=database,
            as_dict=True)
        cursor=db.cursor()

        
        match request.method:
            case "GET":
                return "GET message received"
            case "PUT":
                return "PUT message received"
            case "POST":
               return "POST message received"
            case "DELETE":
                return "DELETE message received"

        #cursor.execute()
        db.close()



    except Exception as e:
        return str(e)

