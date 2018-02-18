from flask import Flask, render_template, request
import folium
from info_serch import pershe

myMap = folium.Map()
app = Flask(__name__)
app.secret_key = "hi"


@app.route('/')
def main():
    return render_template('index.html')


@app.route("/info_return", methods=['POST', 'GET'])
def info_return():
    twi = str(request.args.get('account'))
    result = pershe(twi, request.args.get('info'))
    return render_template("output_info.html", name=result)


if __name__ == "__main__":
    app.run(debug=True)
