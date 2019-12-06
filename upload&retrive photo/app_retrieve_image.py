import os
from flask import Flask, request, render_template, send_from_directory

from src import uploadPhoto
from src.retrievePhoto import readBLOB

app = Flask(__name__, static_folder="temp")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def getID():
    return render_template("retrieve.html")

@app.route("/retrieve", methods=["GET","POST"])
def retrieve():
    if request.method == "POST":
        usr_id = request.form["uid"]
    target = os.path.join(APP_ROOT, 'temp/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)


    usr_id = request.form["uid"]
    filename = "temp.jpg"
    destination = "/".join([target, filename])
    print(usr_id)
    readBLOB(usr_id, destination)

    print("Accept incoming file:", filename)
    print("Save it to:", destination)

    return render_template("complete.html", image_name=destination)

@app.route('/retrieve/<filename>')
def send_image(filename):
    return send_from_directory("temp", filename)


if __name__ == "__main__":
    app.run(port=4555, debug=True)