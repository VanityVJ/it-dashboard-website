from flask import Blueprint, render_template, redirect
from flask_login import login_user, login_required, logout_user, current_user
from flask import Flask, redirect
import os

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/home1')
def home1():
    return render_template("home1.html", user=current_user)

@views.route('/home2')
def home2():
    return render_template("home2.html", user=current_user)

@views.route('/home3')
def home3():
    return render_template("home3.html", user=current_user)


@views.route('/home4', methods=["GET"])
def home4():
    return render_template("home4.html", user=current_user)

@views.route('/home5', methods=["GET"])
def home5():
    return render_template("http://0.0.0.0:8081/", code=302)

import pandas as pd
import matplotlib.pyplot as plt
@views.route('/home6')
def home6():
    filename = 'website/static/DC-Asset-sheet.xlsx'

	# to read the csv file using the pandas library
    data = pd.DataFrame(pd.read_excel(filename, header=None))

    data.style.set_properties(**{"font-size":"10pt", "color":"green"})

    myData = data.values
    return render_template('csv-display.html',  myData=myData, user=current_user ) 

@views.route('/home7')
def home7():
    filename1 = 'website/static/PSMRI-DC_Incident-tracker.xlsx'

	# to read the csv file using the pandas library
    data1 = pd.DataFrame(pd.read_excel(filename1, header=None))

    data1.style.set_properties(**{"font-size":"10pt", "color":"green"})

    myData1 = data1.values
    return render_template('csv-display1.html',  myData1=myData1, user=current_user )



import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template
from io import BytesIO
import base64

@views.route('/home8')
def home8():
    data = pd.read_csv('website\static\graph.csv')
    df = pd.DataFrame(data)

    img = BytesIO()
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])

    # Plot the data using bar() method
    plt.bar(X, Y, color=['g','r','b','y'] )
    
        
    plt.title("HYD DC Total Server and Device Count")
    plt.xticks( rotation= 35)
    plt.ylabel("Number of Devices")
    #plt.plot(X,Y)
    for a,b in zip(X, Y): 
        plt.text(a, b, str(b))
    plt.savefig(img, format='png', dpi=75)
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return f"<img src='data:image/png;base64,{plot_url}'/>"
    # Send the graph as a file
    #return render_template("graph.html", plot_url=plot_url )
