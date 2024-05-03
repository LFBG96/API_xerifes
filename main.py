from flask import Flask
from xerifes import jsonXerifes
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
@cross_origin()
def index():
    return jsonXerifes()


if __name__ == '__main__':
    app.run()