from flask_cors import CORS
from flask import request
from flask import jsonify
from flask import Flask

from chat import res


app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def home():
  ferzan = res(str(request.args.get('message')), "88.227.239.24", 1), 200
  print("ferzan")
  print(ferzan)
  return ferzan


if __name__ == "__main__":
  app.run(debug=True)
