# -*- coding: utf-8 -*-

from flask import Flask,render_template
app=Flask(__name__,template_folder='template')
@app.route('/')
def Chatbot():
    return render_template('Chatbot.html')
@app.route('/about.html')
def about():
    return render_template('about.html')
@app.route('/feedback.html',methods = ['GET','POST'])
def feedback():
    return render_template('feedback.html')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')
if __name__ =='__main__':
    app.run(debug=True)
