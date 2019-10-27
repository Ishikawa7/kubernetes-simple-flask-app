from flask import Flask, request
import random
import http.client
# TODO use "import request" instead of http.cliet

app = Flask(__name__)

@app.route("/")
def hello():
    return "Frontend running"

@app.route('/ep1')
def rand():
    return str(random.randint(1,101))

@app.route('/ep2')
def cpuintensive():
    # TODO set the port for the http connection
    # TODO set a larger timeout for the http request
    connection = http.client.HTTPConnection('backend-cluster-ip-service',port=5000,timeout=100) #("backend-service")
    connection.request("GET", '/bep1')
    response = connection.getresponse()
    print("Status: {} and reason: {}".format(response.status, response.reason))

@app.route('/ep3', methods=['POST'])
def saveondatabase():
    # TODO set the port for the http connection
    # TODO set a larger timeout for the http request
    # TODO add a request body
    connection = http.client.HTTPConnection("backend-cluster-ip-service",port=5000,timeout=100)
    connection.request("POST", "/bep2", body = request.data)
    response = connection.getresponse()
    print("Status: {} and reason: {}".format(response.status, response.reason))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)