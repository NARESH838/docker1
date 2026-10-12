from flask import Flask
import os

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Dockerized web application</h1><p>Running inside a container</p>"

@app.route("/health")
def health():
    return {"status":"healthy"}

@app.route("/info")
def info():
    return {
        "application":"Dockerized web app",
        "environment":os.getenv("ENVIRONMENT","development")
    }

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)