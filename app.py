from flask import Flask, render_template, jsonify, request
import pandas as pd
from io import StringIO, BytesIO
from base64 import b64encode


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


@app.route('/edaanalisis', methods=['POST'])
def analize_data():
    #global data_final
    print("...Función eda analisis")
    res = {}
    name = request.files["file-eda"].filename
    file_content = request.files["file-eda"].read().decode("utf-8")
    if len(file_content) > 0:
        print("Se encuentra archivo")
        type = name.split(".")[-1]
        if type.lower() == "csv":
            Datos = pd.read_csv(StringIO(file_content))
        elif type.lower() == "txt":
            Datos = pd.read_table(StringIO(file_content))
        #Datos = pd.read_csv(StringIO(file_content))
        #data_final = Datos
        Datos
        data_frame = pd.DataFrame(Datos)
        res["eda-table"] = data_frame.to_html(table_id="eda-t")
        dtype = pd.DataFrame(data_frame.dtypes)
        res["dtype"] = dtype.to_html(table_id="eda-dtype")
        res["faltantes"] = pd.DataFrame(data_frame.isnull().sum()).to_html(table_id="eda-null")
        res["describe"] = pd.DataFrame(data_frame.describe()).to_html(table_id="eda-desc")
        res["corr"] = pd.DataFrame(data_frame.corr()).to_html(table_id="eda-corr")
        #labels = Data.config_columnas(list(Datos.columns.values))
    else:
        print("No existe un archivo a analizar")
        raise Warning("No existe un archivo a analizar")
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)
