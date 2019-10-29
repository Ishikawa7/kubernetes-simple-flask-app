from flask import Flask, request
import http.client
import redis

app = Flask(__name__)

# TODO Set the redis host
r = redis.Redis(host="redis-cluster-ip-service")

def count_primes(num = 100000):
    if num < 2:
        return 0
    primes = [2]
    for n in range(2, num + 1):
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
    return str(len(primes))

@app.route("/")
def hello():
    return "Backend running"

@app.route('/bep1')
def cpuintensive():
    return count_primes()
    

@app.route('/bep2', methods=['POST'])
def redisCall():
    r.Set("bodyReceived",str(request.data))
    return("Successfull!")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)