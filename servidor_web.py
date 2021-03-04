from flask import Flask, json, request, jsonify
from GUI_MySQL_class import MySQL

app = Flask(__name__)

mysql = MySQL()

@app.route("/")
def server_info():
    rv = mysql.ConsultData()
    return jsonify(rv)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True,
            threaded=True, use_reloader=False)