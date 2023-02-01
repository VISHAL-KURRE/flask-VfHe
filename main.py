from flask import Flask, jsonify, render_template
import os
import templates

# app = Flask(__name__  )
app = Flask(__name__  , template_folder='templates', static_folder='static')

template_folder='templates'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
