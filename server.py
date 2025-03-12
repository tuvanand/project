from flask import Flask, jsonify, request
import json

app = Flask('__name__')

@app.route('/', methods=['POST','GET']) 
def api():
    if request.method == 'POST':
        payload = request.method
        print("Testing it works")
        print(payload)
        return payload, 200
    elif request.method == 'GET':
        # Handle GET request: return readme2.json and print "helloworld2"
        print("helloworld")
        response_data ={
            "message": "This is the README for GET"
        }
        return jsonify(response_data), 200
if __name__ == '__main__':
    #app.run(ssl_context=('cert.pem','key.pem'), host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000)