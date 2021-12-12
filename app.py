from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/eda')
def eda_template():
    return render_template('eda.html')
    
@app.route('/select_caract')
def caract_template():
    return render_template('select_caract.html')

@app.route('/clustering')
def cluster_template():
    return render_template('clustering.html')

@app.route('/re_asociacion')
def re_asociacion_template():
    return render_template('re_asociacion.html')

@app.route('/a_decision')
def a_decision_template():
    return render_template('a_decision.html')

if __name__ == "__main__":
    app.run(debug=True)
