from flask import Flask, render_template, redirect, jsonify, request
import os
from twilio.rest import Client

app =  Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sendSignal", methods=["POST"])
def sendSms():

    queryString = request.data.decode("utf-8")

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = "AC5f50fcb83ef0f581fb76dd4cf8bb7ec0"
    auth_token = "c3578752fa0b97e5d7cc876f3a896c71"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=f"query String: {queryString}",
                        from_='+16187624574',
                        to='+18322787527'
                    )

    print(message.sid)

    return jsonify({'result':"Done"})


if __name__ == "__main__":
    app.run(debug=True)