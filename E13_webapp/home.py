from flask import Flask, render_template
from E11_import.hs_student import HighSchoolStudent


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


app.run(debug=True)
