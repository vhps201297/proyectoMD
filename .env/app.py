from flask import Flask

app = Flask(__name__)

@app.route('/pca')
def pca():
    return 'pca'

@app.route('/')
def home():
    return render_template("templates/index.html", None)
