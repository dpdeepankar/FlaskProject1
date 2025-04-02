import pymongo
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()


MONGO_URI=os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

db = client.sample
collection = db['flask_tutorial']

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.json)
    try:
        print("Adding data to DB")
        collection.insert_one(form_data)
        print("Data added")
        print(form_data)
        return jsonify({"Status": "Success"})
    except Exception as e:
        return jsonify({"Error": str(e)})


@app.route('/view')
def view():
    data = list(collection.find())

    for item in data:
        print(item)
        del item['_id']
    data = { "data":data }

    return data


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
