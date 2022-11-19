# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 00:29:31 2022

@author: Yuvan Shankar J
"""

from flask import Flask,render_template
from flask import *
from cloudant.client import Cloudant
from cloudant.result import Result
app=Flask(__name__)
ACCOUNT_NAME = "74067243-5251-41ca-89ed-979e65c1cbd2-bluemix"
API_KEY = "IqWgY3pe1n9DGN4pN_9uSXzmlCs27ML4DkcTAePwkFbv"

client = Cloudant.iam(ACCOUNT_NAME,API_KEY,connect=True)
mydatabase = client.create_database('feedback')
if mydatabase.exists():
    print(" successfully created.\n")

@app.route('/')
def Chatbot():
    return render_template('Chatbot.html')

@app.route('/home')
def home():
    return render_template('Chatbot.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/feedback',methods = ['GET','POST'])
def feedback():
    print("******")
    if request.method == "POST":
        email = request.form['mail']
        name = request.form['name']
        num = request.form['num']
        place= request.form['place']
        msg = request.form['message']
        #print(email,name,num,place,msg)
        jsonDocument= {
            'email':email,
            'name':name,
            'contact_number':num,
            'place':place,
            'feedback':msg
            }
        newDocument = mydatabase.create_document(jsonDocument)
        result = Result(mydatabase.all_docs,include_docs=True)
        print(result[0])
        return redirect(url_for('home'))
        print('#####')
    return render_template('feedback.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
######
mydatabase1 = client.create_database('net_banking')
if mydatabase1.exists():
    print(" successfully created.\n")
@app.route('/netbanking',methods = ['GET','POST'])
def netbanking():
    print("******")
    if request.method == "POST":
        email = request.form['mail']
        name = request.form['name']
        acc_num = request.form['num']
        contact_number=request.form['number']
        date_of_birth=request.form['dob']
        date_of_application=request.form['doa']
        viewing_rights=request.form['viewing']
        transaction_rights=request.form['transaction']
        type_of_account=request.form['type']
        jsonDocument= {
            'email':email,
            'name':name,
            'account_number':acc_num,
            'contact_numer':contact_number,
            'viewing rights':viewing_rights,
            'transactions_rights':transaction_rights,
            'date_of_birth':date_of_birth,
            'date_of_application':date_of_application,
            'type':type_of_account
            }
        newDocument = mydatabase1.create_document(jsonDocument)
        result = Result(mydatabase1.all_docs,include_docs=True)
        print(result[0])
        return redirect(url_for('home'))
        print('#####')
    return render_template('netbanking.html')
mydatabase2=client.create_database('account_balance')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        account_number=request.form['accnum']
        password=request.form['pass']
        account_found=False
        for documents in mydatabase2:
            if documents['account_number']==account_number:
                if documents['password']==password:
                     flash_name='Welcome'+' '+documents['customer_name']+'!'
                     flash(flash_name)
                     flash_text='Your account balance is'+' '+"Rs."+documents['account_balance']
                     flash(flash_text)
                else:
                     flash('INVALID PASSWORD!')
                account_found=True
                break
        if not account_found:
            flash('INVALID ACCOUNT NUMBER!')
    return render_template('login.html')  
if __name__ =='__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)