from flask import Flask, redirect
import os
app = Flask('')

@app.after_request
def treat_as_plain_text(response):
    response.headers["content-type"] = "text/plain"
    return response


@app.route('/')
def home():
  return {"version": "0.2"}

@app.route('/latest')
def latest():
    return "https://cdn.discordapp.com/attachments/844345665688698891/844345684786544640/0.2.zip"

@app.route('/plugins/test')
def plugins_test():
    return "https://cdn.discordapp.com/attachments/834547119129624636/844272126210867240/test-tc.zip"

app.run(host="0.0.0.0",port=8080)