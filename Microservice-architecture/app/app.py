from flask import Flask, request, jsonify
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from gunicorn import *

app = Flask(__name__)

class Phone(BaseModel):
    TypeID: int = 0
    CountryCode: int = 0
    Operator: int = 0
    Number: int = 0

class Contact(BaseModel):
    ID: int = 0
    Username: str = ""
    GivenName: str = ""
    FamilyName: str = ""
    Phone: List[str] = []
    Email: List[str] = []
    Birthdate: date = date.today()

class Group(BaseModel):
    ID: int = 0
    Title: str = ""
    Description: str = ""
    Contacts: List[int] = []

@app.route('/api/v1/contact', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_contact():
    if request.method == 'POST':
        data = request.get_json()
        Contact.model_validate(data)
        return jsonify(Contact().model_dump()), 201
    else:
        return jsonify(Contact().model_dump())

@app.route('/api/v1/group', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_group():
    if request.method == 'POST':
        data = request.get_json()
        Group.model_validate(data)
        return jsonify(Group().model_dump()), 201
    else:
        return jsonify(Group().model_dump())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6080)