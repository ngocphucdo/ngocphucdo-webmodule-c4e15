from flask import Flask, render_template

from models.service import Service

import mlab

mlab.connect()

app = Flask(__name__)

@app.route('/search')
def search():
    service = Service.objects.get(id='5a956301308e841354e3d00c')
    service.delete()
    return render_template('ex2.html', service = service)


if __name__ == '__main__':
  app.run(debug=True)
