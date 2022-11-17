from flask import Flask,render_template,request,redirect,url_for
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import requests
from tensorflow.python.keras.backend import set_session
import os
from tensorflow.keras.preprocessing import image
import pandas as pd
import tensorflow as tf
from werkzeug.utils import secure_filename
app = Flask(__name__, instance_relative_config=True)
model = load_model("mnistCNN.h5")
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict.html')
def prediction():
    return render_template('predict.html')
@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method =='POST':
        f = request.files['image']
        basepath= os.path.dirname(__file__)
        file_path=os.path.join(basepath,'data',secure_filename(f.filename))
        f.save(file_path)
        img = Image.open(file_path).convert("L")
        img=img.resize((28,28))
        im2arr=np.array(img)
        im2arr=im2arr.reshape(1,28,28,1)
        y_pred=np.argmax(model.predict(im2arr))
        print(y_pred)
        df=pd.read_excel('digitpred.xlsx')
        loader=print(df.iloc[y_pred]['digits'])
       
    else:
        return none
    return df.iloc[y_pred]['digits']


if __name__=='__main__':
  app.run(host='0.0.0.0',port=5000,debug=True)

