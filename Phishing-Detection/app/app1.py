
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))


@app.route("/", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        links = [
        {
            'predict': 'http://127.0.0.1:5000/'
        }
        ]
        time_domain_activation = int(request.form['time_domain_activation'])
        qty_questionmark_file = int(request.form['qty_questionmark_file'])
        qty_slash_file = int(request.form['qty_slash_file'])
        qty_questionmark_directory = int(request.form['qty_questionmark_directory'])
        qty_hashtag_directory = int(request.form['qty_hashtag_directory'])
        qty_dollar_file = int(request.form['qty_dollar_file'])
        qty_slash_directory = int(request.form['qty_slash_directory'])
        qty_slash_url = int(request.form['qty_slash_url'])
        qty_hashtag_file = int(request.form['qty_hashtag_file'])
        directory_length = int(request.form['directory_length'])
        
        prediction=model.predict([[time_domain_activation, qty_questionmark_file,qty_slash_file,qty_questionmark_directory, qty_hashtag_directory,qty_dollar_file, qty_slash_directory, qty_slash_url,qty_hashtag_file, directory_length]])
        output=np.round(prediction)
        if output==0:
            return render_template('index.html',links=links,prediction_text="The website is not a phishing website")
        else:
            return render_template('index.html',links=links,prediction_text="The website is a phishing website")
    else:
        links = [
        {
            'predict': 'http://127.0.0.1:5000/'
        }
        ]
        return render_template('index.html',links=links)

if __name__=="__main__":
    app.run()