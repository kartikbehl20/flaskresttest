from flask import Flask
from flask_restful import request,Api,Resource
import json
import os
app = Flask(__name__)
user_data = [{'id': 1, 'email': 'george.bluth@reqres.in', 'first_name': 'George', 'last_name': 'Bluth', 'avatar': 'https://reqres.in/img/faces/1-image.jpg'},
              {'id': 2, 'email': 'janet.weaver@reqres.in', 'first_name': 'Janet', 'last_name': 'Weaver', 'avatar': 'https://reqres.in/img/faces/2-image.jpg'},
              {'id': 3, 'email': 'emma.wong@reqres.in', 'first_name': 'Emma', 'last_name': 'Wong', 'avatar': 'https://reqres.in/img/faces/3-image.jpg'},
              {'id': 4, 'email': 'eve.holt@reqres.in', 'first_name': 'Eve', 'last_name': 'Holt', 'avatar': 'https://reqres.in/img/faces/4-image.jpg'},
              {'id': 5, 'email': 'charles.morris@reqres.in', 'first_name': 'Charles', 'last_name': 'Morris', 'avatar': 'https://reqres.in/img/faces/5-image.jpg'},
              {'id': 6, 'email': 'tracey.ramos@reqres.in', 'first_name': 'Tracey', 'last_name': 'Ramos', 'avatar': 'https://reqres.in/img/faces/6-image.jpg'}]

@app.route("/Books",methods=["GET"])
def books():
    return json.dumps(user_data)

@app.route("/Books/<int:bookid>",methods=["GET","POST"])
def book_id(bookid):
    if request.method == "POST":
        print(request.form.get("name"))
        return 'created',201
    else:
        for row in user_data:
            if row.get("id") == bookid:
                return row,200
        else:
            return 'not found',400

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")



