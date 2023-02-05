
from flask import Flask,request, jsonify, render_template
import os
import templates

# app = Flask(__name__  )
app = Flask(__name__  , template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = "My secret key"
template_folder='templates'


@app.route('/', methods = ['GET', "POST"])
def index():

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))




