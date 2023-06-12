from flask import Flask , render_template
from api.resource import User ,api


app=Flask(__name__)
api.init_app(app)


@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/ppt2text")
def ppt2text():
    return render_template("ss.html")

app.run()
