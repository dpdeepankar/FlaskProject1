from flask import Flask, request, render_template, jsonify
import requests


app = Flask(__name__)

BACKEND_URL="http://192.168.71.144:5001"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    response = requests.post(BACKEND_URL+'/submit', json=form_data)
    return jsonify(response.json())

@app.route('/get-data')
def view():
    response = requests.get(BACKEND_URL + '/view')
    return response.json()


if __name__  == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

