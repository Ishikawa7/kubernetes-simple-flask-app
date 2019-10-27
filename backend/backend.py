from flask import Flask
import http.client
#import redis

app = Flask(__name__)

# TODO Set the redis host
#redis = redis.Redis(host="myredis-server")

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
    

#@app.route('/bep2')
#def redisCall():
#    redis.incr("counter")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)