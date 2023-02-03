import flask_wtf
from flask import Flask,request, jsonify, render_template
import os
import templates
from ozekilibsrest import Configuration, Message, MessageApi
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired




# app = Flask(__name__  )
app = Flask(__name__  , template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = "My secret key"
template_folder='templates'

# ozekilibsrest messages
configuration = Configuration(
    username="http_user",
    password="qwe123",
    api_url="http://127.0.0.1:9509/api"
)
api = MessageApi(configuration)
logs = []





# Create a form
class contactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    project = StringField("project", validators=[DataRequired()])
    messgae = StringField("message", validators=[DataRequired()])
    Submit = SubmitField("Submit")


def index1():
     print("index1")
     return "test"

@app.route('/', methods = ['GET', "POST"])
def index():
    if request.method == 'POST':

        _form = request.form
        print(_form)
        email = str(_form["email"])
        name = str(_form["name"])
        project = str(_form["project"])
        message = str(_form["message"])
    to_address = "+1 5419080576"
    message = Message(
        to_address=request.form['to_address'],
        text=request.form['text']
    )
    log = api.send(message)
    logs.append(log)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))




