from flask import Flask, json, request
import base64
import mysql
from gevent import pywsgi
app = Flask(__name__)


@app.route("/")
def index():
    v0 = {"code": 0, "msg": "易下服务端运行中"}
    return json.dumps(v0, ensure_ascii=False)


@app.route("/cx", methods=["POST"])
def cx():
    for1 = request.form.get("sql")
    for1=for1.replace("%B1","+")
    v0 = mysql.cx(for1)
    if v0["code"] == 200:

        return v0, 200
    else:
        return v0, 400


@app.route("/zx", methods=["POST"])
def zx():
    for1 = request.form.get("sql")
    for1=for1.replace("%B1","+")
    print(for1)

    v0 = mysql.zx(for1)
    if v0["code"] == 200:
        return json.dumps(v0, ensure_ascii=False), 200
    else:
        return json.dumps(v0, ensure_ascii=False), 400


if __name__ == "__main__":
    server = pywsgi.WSGIServer(('0.0.0.0', 5001), app)
    server.serve_forever()
    print("易下数据库启动成功")