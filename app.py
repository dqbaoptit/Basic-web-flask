from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route("/info", methods=['POST'])
def log():
  username = request.form.get('username')
  password = request.form.get('password')
  if(username == "admin" and password =="admin"):
    return render_template('logged.html')
  else :
    return render_template('fault.html')