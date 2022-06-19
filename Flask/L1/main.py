from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = "hXDm8NXqqJATH&7XHW6AtM.XEqM4cEMn"


@app.route('/')
def hello():
    if not'good' in session:
        session['good'] = 0
        session['bad'] = 0

        msg1 = "いい人 " + str(session['good']) + "人"
        msg2 = "良くない人 " + str(session['bad']) + "人"
        return render_template('Sample2.html', message1=msg1, message2=msg2)


@app.route('/Sample2',methods = ['POST','GET'])
def Sample2() :
    if not'good' in session :
        session['good'] = 0
        session['bad'] = 0
    if request.method == "GET" :
        session['good'] += 1
    else:
        session['bad'] += 1
    msg1 = "いい人 " + str(session['good']) + "人"
    msg2 = "良くない人 " + str(session['bad']) + "人"
    return render_template('Sample2.html', message1=msg1, message2 = msg2)
if __name__ == '__main__':
    app.run(debug = True)
