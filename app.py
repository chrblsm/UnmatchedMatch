from flask import Flask, render_template, redirect, jsonify, request
import os
from twilio.rest import Client
import time

app =  Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sendSignal", methods=["POST"])
def sendSms():

    queryString = request.data.decode("utf-8")

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=f"query String: {queryString}",
                        from_='+',
                        to='+'
                    )

    print(message.sid)

    time.sleep(240)

    return jsonify({'result':"Done"})


if __name__ == "__main__":
    app.run(debug=True)
