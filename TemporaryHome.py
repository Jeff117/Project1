# Author: Jeff San Paolo
# Description: Homepage used as a template to ensure my pages work as designed
# $env:FLASK_APP = "TemporaryHome.py"
# $env:FLASK_DEBUG = "1"
# flask run

from flask import Flask, render_template,url_for,request,redirect
from flask_bootstrap import Bootstrap
from PIL import Image
from NewHome import *
app = Flask(__name__)
Bootstrap(app)


@app.route('/Report')
def ReportAnimals():
    return render_template('ReportAnimals.html')

@app.route('/Search')
def SearchAnimals():
        return render_template('SearchAnimals.html')

@app.route('/Searchs', methods = ['POST'])
def SearchAnimal(dogname):
    return render_template('SearchAnimals.html',
    Animallist = Animal_search(dogname[0],dogname[1],dogname[2]), doit = "yes")
