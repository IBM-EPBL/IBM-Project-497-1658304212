# -*- coding: utf-8 -*-
from flask import Flask,render_template
app=Flask(__name__,template_folder='template')
@app.route('/',methods = ['GET','POST'])
def Chatbot():
    return render_template('Chatbot.html')
def about():
    return render_template('about.html')
def feedback():
    return render_template('feedback.html')
def contact():
    return render_template('contact.html')
if __name__ =='__main__':
    app.run(debug=True)

