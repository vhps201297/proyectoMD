from flask import Flask, render_template, jsonify, request
from sklearn.preprocessing import StandardScaler, MinMaxScaler  
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
from io import StringIO, BytesIO
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from base64 import b64encode
from matplotlib import rcParams
import seaborn as sns

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
    res = {}
    name = request.files["file-eda"].filename
    file_content = request.files["file-eda"].read().decode("utf-8")
    if len(file_content) > 0:
        type = name.split(".")[-1]
        if type.lower() == "csv":
            Datos = pd.read_csv(StringIO(file_content))
        elif type.lower() == "txt":
            Datos = pd.read_table(StringIO(file_content))
        data_frame = pd.DataFrame(Datos)
        res["eda-table"] = data_frame.to_html(table_id="eda-t")
        dtype = pd.DataFrame(data_frame.dtypes)
        res["dtype"] = dtype.to_html(table_id="eda-dtype")
        res["faltantes"] = pd.DataFrame(data_frame.isnull().sum()).to_html(table_id="eda-null")
        res["describe"] = pd.DataFrame(data_frame.describe()).to_html(table_id="eda-desc")
        res["corr"] = pd.DataFrame(data_frame.corr()).to_html(table_id="eda-corr")
        res["heapmap"] = getHeapMap(Datos)
    else:
        print("No existe un archivo a analizar")
        raise Warning("No existe un archivo a analizar")
    return jsonify(res)

@app.route('/sc-corr', methods=['POST'])
def analize_sc_pca():
    resp = {}
    name = request.files["file-sc"].filename
    file_content = request.files["file-sc"].read().decode("utf-8")
    if len(file_content) > 0:
        type = name.split(".")[-1]
        if type.lower() == "csv":
            Datos = pd.read_csv(StringIO(file_content))
        elif type.lower() == "txt":
            Datos = pd.read_table(StringIO(file_content))
        data_frame = pd.DataFrame(Datos)
        resp["sc-table"] = data_frame.to_html(table_id="tsc-table")
        
        dtype = pd.DataFrame(data_frame.dtypes)
        resp["sc-dtype"] = dtype.to_html(table_id="tsc-dtype")
        resp["sc-faltantes"] = pd.DataFrame(data_frame.isnull().sum()).to_html(table_id="tsc-null")
        resp["sc-corr"] = pd.DataFrame(data_frame.corr()).to_html(table_id="tsc-corr")
        resp["heapmap"] = getHeapMap(Datos)
        
    else:
        print("No existe un archivo a analizar")
        raise Warning("No existe un archivo a analizar")
    return jsonify(resp)
    
@app.route('/sc-pca', methods=['POST'])
def analize_sc():
    resp = {}
    name = request.files["file-pca"].filename
    file_content = request.files["file-pca"].read().decode("utf-8")
    if len(file_content) > 0:
        type = name.split(".")[-1]
        if type.lower() == "csv":
            Datos = pd.read_csv(StringIO(file_content))
        elif type.lower() == "txt":
            Datos = pd.read_table(StringIO(file_content))
        data_frame = pd.DataFrame(Datos)
        resp["clust-table"] = data_frame.to_html(table_id="id-tdata")
        
        
    else:
        print("No existe un archivo a analizar")
        raise Warning("No existe un archivo a analizar")
    return jsonify(resp)

@app.route('/clust-kmeans', methods=['POST'])
def analize_kmeans():
    resp = {}
    name = request.files["file-cluster"].filename
    n_clust = int(request.form["n_clust"])
    
    file_content = request.files["file-cluster"].read().decode("utf-8")
    if len(file_content) > 0:
        type = name.split(".")[-1]
        if type.lower() == "csv":
            Datos = pd.read_csv(StringIO(file_content))
        elif type.lower() == "txt":
            Datos = pd.read_table(StringIO(file_content))
        data_frame = pd.DataFrame(Datos)
        resp["clust-table"] = data_frame.to_html(table_id="id-tdata")
        
        vModel = Datos.values
        MParticional = KMeans(n_clusters=n_clust, random_state=0).fit(vModel)
        MParticional.predict(vModel)
        Datos['clusterP'] = MParticional.labels_
        n_elem = Datos.groupby(['clusterP'])['clusterP'].count()
        resp['n_elements']  = pd.DataFrame(n_elem).to_html(table_id='id-nelem')
        CentroidesP = pd.DataFrame(MParticional.cluster_centers_)
        resp["centroid"] = CentroidesP.to_html(table_id='id-cen')
    else:
        print("No existe un archivo a analizar")
        raise Warning("No existe un archivo a analizar")
    return jsonify(resp)

@app.route('/clust-jerarq', methods=['POST'])
def analize_clust_jerar():
    resp = {}
    name = request.files["file-cluster"].filename
    n_clust = int(request.form["n_clust"])
    
    file_content = request.files["file-cluster"].read().decode("utf-8")
    if len(file_content) > 0:
        type = name.split(".")[-1]
        if type.lower() == "csv":
            Datos = pd.read_csv(StringIO(file_content))
        elif type.lower() == "txt":
            Datos = pd.read_table(StringIO(file_content))
        data_frame = pd.DataFrame(Datos)
        resp["clust-table"] = data_frame.to_html(table_id="id-tdata")
        
        estandarizar = StandardScaler()                               # Se instancia el objeto StandardScaler o MinMaxScaler 
        MEstandarizada = estandarizar.fit_transform(np.array(data_frame))   # Se calculan la media y desviación y se escalan los datos
        #Arbol = shc.dendrogram(shc.linkage(MEstandarizada, method='complete', metric='euclidean'))
        MJerarquico = AgglomerativeClustering(n_clusters=n_clust, linkage='complete', affinity='euclidean')
        MJerarquico.fit_predict(MEstandarizada)
        Datos['clusterH'] = MJerarquico.labels_
        n_elem = Datos.groupby(['clusterH'])['clusterH'].count() 
        resp['n_elements'] = pd.DataFrame(n_elem).to_html(table_id='id_nelem')
        resp["centroid"] = data_frame.groupby('clusterH').mean().to_html(table_id='id_cen')
        
    else:
        print("No existe un archivo a analizar")
        raise Warning("No existe un archivo a analizar")
    return jsonify(resp)


def getHeapMap(dataset):
    plt.figure(figsize=(28,8))
    rcParams.update({'figure.autolayout': True})
    sns.heatmap(dataset.corr(), cmap='RdBu_r', annot=True)
    b, t = plt.ylim() # discover the values for bottom and top
    b += 0.5 # Add 0.5 to the bottom
    t -= 0.5 # Subtract 0.5 from the top
    plt.ylim(b, t) # update the ylim(bottom, top) values
    pic_IObytes = BytesIO()
    plt.savefig(pic_IObytes,format='png')
    pic_IObytes.seek(0)
    pic_hash = b64encode(pic_IObytes.read())
    image = """<img src="data:image/png;base64,{b64}" style="width: 1000px;height: 400px;"/>"""
    heap_complete = image.format(b64=pic_hash.decode("utf-8"))
    return heap_complete

if __name__ == "__main__":
    app.run(debug=True)
