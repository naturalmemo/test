from urllib import request
from flask import Flask, render_template
# ,request
app = Flask(__name__)
# app_seclet_key = "AAA"

@app.route("/")
# @app.route("/index")

def index():
        name = request.args.get("name")
        prefecture =  request.args.get("prefecture")
        city = request.args.get("city")
    # page = request.args.get("page")
    # number = request.args.get("number")
        return render_template('index.html',name=name,prefecture=prefecture,city=city)
# render_template("q_1.html", name=name, prefecture=prefecture,
                        #    city=city)
@app.route("/index",methods=["GET"])
def q_1():
        # request.args.get("name")
    return render_template('q-1.html')
if __name__ == "__main__":
    app.run(debug=True)
''''
@app.route("/q-2")
def q_2():
    return render_template('q-2.html')
@app.route("/q-3")
def q_3():
    return render_template('q-3.html')
@app.route("/q-4")
def q_4():
    return render_template('q-4.html')
@app.route("/q-5")
def q_5():
    return render_template('q-5.html')



if __name__ == "__main__":
    app.run(debug=True)


@app.route("/index", methods=["POST"])
def post():
    name = request.form["name","prefecture","city"]
    return render_template("q_1.html")
if __name__ == "__main__":
    app.run(debug=True)'''