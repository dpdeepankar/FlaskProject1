from flask import Flask, request

app = Flask(__name__)

@app.route('/api')
def home():
    with open('backendfile.txt','r') as f:
        data = f.read()

    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

