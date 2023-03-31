# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define route and Verify_otp() function below

def verify_otp():










        verification = client.verify \
            .services('Enter service sid from twilio') \
            .verifications \
            .create(to=enter mobile number variable here, channel='Enter mode of sending otp here')










if __name__ == "__main__":
    app.run()

