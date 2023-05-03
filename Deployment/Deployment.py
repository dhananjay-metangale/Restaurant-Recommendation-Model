# Importing Python Libraries  
import os
import pandas as pd 
import numpy as np 
from markupsafe import escape
# Importing Flask To Deploy Project On WebPage
import flask
import pickle
from flask import Flask, render_template, request
# The Following Library connects all the ipynb files and Python Files Together

from importnb import imports 
with imports("ipynb"):
    import output1
# Calling The Dictionaries From Dictionaries.py
import dictionaries 
cuidict = dictionaries.cuisinedict
addict = dictionaries.Addressdict

# Initializing Flask
app=Flask(__name__)
loaded_model = pickle.load(open('MLProject.pkl','rb')) # Calling The Price Recommendation model 
model2 = pickle.load(open('rfc_model.pkl','rb')) # Calling The Location Recommendation model
@app.route('/')
def home():
    print('home')
    return render_template('index.html')
loc = ''
keyword = ''
@app.route('/predict',methods = ['POST'])
def result():
    if request.method == 'POST':
        print('predicting1')
        cuisine = request.form.get('cuisine') # It Takes Cuisine From Webpage
        
        price_for_one = request.form.get('price_for_one') # It Users Takes Price For One
        print('predicting3')
     
        Preferred_Location = request.form.get('Preferred_Location') # It Takes The Location
        print(Preferred_Location)
        lst1 = output1.main2(Preferred_Location,cuisine) # This Initializes The Main Function Of Output.ipynb File That Generates The Insights
        location = lst1[0]
        cuis = lst1[1]
        a = 1
        b = 1
        for j in cuidict.keys(): # Searches For The Encoded Value Of Cuisine In Cuisine Dict
            if(cuis==j):
                print(j)
                a = cuidict.get(j)*b
        for i in addict.keys(): # Searches For The Encoded Values Of Address In Address Dict 
            if(location==i):
                print(i)
                b = addict.get(i)*b
        print(location,cuis)
        lst = output1.main(loc = Preferred_Location, keyword = cuisine)
        print(lst)
        c = lst[0]
        output = loaded_model.predict([[a, b, c]]) # Predicts The Price as Per The Pickle File
        out = model2.predict([[a,price_for_one,c]])[0] # Predicts The Location as per The Pickle File
        print(out)
        locout = [i for i in addict if addict[i] == out] # Retraces The Address Predicted by model in address dict
        print(locout)
        return render_template('prediction.html',prediction=output[0],locationpred = locout[0], prediction1=round(lst[0],2),prediction2=lst[1],prediction3=lst[2],prediction4=lst[3],
                              prediction5=lst[-1]) # Directs To The  Landing Page

if __name__ == '__main__': # Initializing The Flask
    app.run(debug=True)