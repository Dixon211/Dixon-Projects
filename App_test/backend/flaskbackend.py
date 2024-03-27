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
            database=database)
        cursor=db.cursor()

        
        match request.method:
            case "GET":
                cursor.execute("SELECT COUNT(MACAddress) FROM Machine WHERE MACAddress = %s", (recieved[0]["MACAddress"],))
                result = cursor.fetchone()
                return str(result)
            case "POST":
                cursor.execute("INSERT INTO Machine (DefaultGateway, LocalAddress, MACAddress, MachineName) VALUES ('%s', '%s', '%s', '%s');" % (recieved[0]["DefaultGateway"], recieved[0]["LocalAddress"], recieved[0]["MACAddress"], recieved[0]["MachineName"]))
                db.commit()
                return f"POST received"
            case "PUT":
               cursor.execute("UPDATE Machine SET DefaultGateway= '%s', LocalAddress= '%s', MachineName= '%s' WHERE MACAddress = '%s';" % (recieved[0]["DefaultGateway"], recieved[0]["LocalAddress"], recieved[0]["MachineName"], recieved[0]["MACAddress"]))
               db.commit()
               return "PUT message received"
            case "DELETE":
                return "DELETE message received"

        db.close()



    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
