# Author: Jeff San Paolo
# Description: Homepage used as a template to ensure my pages work as designed
# $env: FLASK_APP = "TemporaryHome.py"
# $nv:FLASK_DEBUG = "1"
# flask run

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image

app = Flask(__name__)
Bootstrap(app)

@app.route('/Search')
def SearchAnimals():
    return render_template('SearchAnimals.html')

@app.route('/Report')
def ReportAnimals():
    return render_template('ReportAnimals.html')
