from flask import Flask, render_template, jsonify, request
import pandas as pd
from io import StringIO, BytesIO


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


@app.route("/create_table", methods=["POST"])
def analize_data():
    global data_final
    response = {}
    name = request.files["file"]
    file_content = request.files["file"].read().decode("utf-8")
    if len(file_content) > 0:
        type = (name.filename).split(".")[-1]
        if type.lower() == "csv":
            Datos = pd.read_csv(StringIO(file_content))
        elif type.lower() == "txt":
            Datos = pd.read_table(StringIO(file_content))
        #Datos = pd.read_csv(StringIO(file_content))
        data_final = Datos
        data_frame = pd.DataFrame(Datos)
        HTML = frame.to_html().replace("dataframe","table table-bordered")
        HTML = HTML.replace('border="1"','id="table1"')
        labels = Data.config_columnas(list(Datos.columns.values))
    else:
        raise Warning("No existe un archivo a analizar")
    return jsonify(HTML,labels)

if __name__ == "__main__":
    app.run(debug=True)
