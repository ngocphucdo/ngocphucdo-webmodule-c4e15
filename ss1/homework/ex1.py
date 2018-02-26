from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/aboutme')
def Myinfo():
    return render_template('Myinfo.html' )

@app.route('/school')
def school():
    return redirect("http://techkids.vn" , code=302)

if __name__ == '__main__':
  app.run(debug=True)
