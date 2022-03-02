from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin

from spellcorrector import spell_corrector

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    data = request.json['data']
    result = spell_corrector(data)
    return jsonify({ "text" : result})


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=port)
    app.run(host='127.0.0.1', port=7000, debug=True)