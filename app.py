#      Teleport Investments Limited 
#
#          Teleport Version 1.0
#
# Objective:
#
# Requirements

from flask import Flask


app = Flask(__name__)

@app.route("/")

def wormhole():
  return "Teleport Investments Limited"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)