import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app=application

##import ridge regressor and standard scaler picke
ridge_model=pickle.load(open('Models/ridge.pkl', 'rb'))
standard_scaler=pickle.load(open('Models/scaler.pkl', 'rb'))


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        try:
            Temperature = float(request.form['Temperature'])
            RH = float(request.form['RH'])
            Ws = float(request.form['Ws'])
            Rain = float(request.form['Rain'])
            FFMC = float(request.form['FFMC'])
            DMC = float(request.form['DMC'])
            ISI = float(request.form['ISI'])
            Classes = float(request.form['Classes'])
            Region = float(request.form['Region'])

            cols = ['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'ISI', 'Classes', 'Region']
            df = pd.DataFrame([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]], columns=cols)

            # Transform using the DataFrame
            new_data_scaled = standard_scaler.transform(df)
            result = ridge_model.predict(new_data_scaled)
            return render_template('home.html', results=result[0])
        except Exception as e:
            return f"Backend Error: {str(e)}"
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")