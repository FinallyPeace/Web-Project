# 請確保終端機位置正確，才能使用 
# ex: PS D:\WebProject

from flask import Flask, render_template
app = Flask(__name__, template_folder='.')

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/page/jp")
def hello_ppp():
    return render_template("page/jp/index.html")