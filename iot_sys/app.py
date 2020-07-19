from time import time

from flask import Flask, request, jsonify, send_from_directory

from model import Model

app = Flask(__name__)


@app.route('/')
def hello_world():
    # pass
    return 'Hello World!'


@app.route('/upload', methods=['get', 'post'])
def upload():
    img = request.files['images']
    filename = str(time()) + '.' + img.filename.split('.')[-1]
    img.save('./static/' + filename)
    return jsonify(msg='上传成功', filename=filename)


@app.route('/predict', methods=['get', 'post'])
def predict():
    filename = request.json.get('filename')
    filepath = './static/' + filename
    model = Model()
    model.predict(filepath)
    return jsonify(msg='预测成功', filename=filename)


# http://127.0.0.1:5000/imgs/1595126621.0030687.jpg
@app.route('/imgs/<string:filename>')
def imgs(filename):
    return send_from_directory('./static/', filename)


if __name__ == '__main__':
    app.run()
