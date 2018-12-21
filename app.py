#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pickle
from flask import Flask, jsonify, request
import pandas as pd

# In[3]:


app = Flask(__name__)
@app.route('/',methods=['GET'])
def test():
    return jsonify({'message' : 'It works'})

@app.route('/predict', methods=['POST'])
def apicall():
    test = request.data 
    loaded_model = None
    with open('/home/harsh/Desktop/moodcafe/model_v1.pk','rb') as f:
       loaded_model =  pickle.load(f)
    censored = loaded_model.censor(test)
    return (censored)
if __name__ == '__main__':
    app.run(debug=True,port = 5000)
    


# In[ ]:




