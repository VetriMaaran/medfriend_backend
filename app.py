import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, jsonify, request

from medicalRecords import returnRecord

cred = credentials.Certificate("service.json")
firebase_admin.initialize_app(cred)
fireStore = firestore.client()


db = fireStore.collection('T5vjG1a7ciY0mOjgyRxAtV8MXmq1').stream()
for data in db:
    print(data.to_dict()['bloodPressure'])
    break

app = Flask(__name__)


@app.route('/fetch/<string:value>')
def simulation(value):
    return jsonify({"message": "success", "data": returnRecord(value)})


@app.route('/webhook')
def webhook_call():
    response = request.get_json()
    print(response)
    return 'null'
