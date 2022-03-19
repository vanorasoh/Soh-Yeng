#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install flask


# In[2]:


from flask import Flask, request, render_template


# In[3]:


app = Flask(__name__) #__name__ => to make sure it is yoursb


# In[4]:


import joblib


# In[5]:


# dir(app)
#route by default look for .html. @app - declarator - indicate must run this function first before running the codes below
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST": #this happens after pressing button submit
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBS_Reg")
        pred = model.predict([[float(rates)]])
        s = "The predicted DBS share price is " + str(pred)
        return(render_template("index.html", results=s))
    else:
        return(render_template("index.html", results="2")) #this happens before pressing button submit
        


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:




