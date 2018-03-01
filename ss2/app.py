from flask import Flask, render_template

from models.service import Service

import mlab

mlab.connect()

app = Flask(__name__)

# service = Service(name='Kieu Anh', yob=1998, gender=0, height=160,
#                 phone="09696969696", address="Ha Noi", status=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<gender>')
def search(gender):
    service = Service.objects(gender=gender, address__exact="Ha Noi", yob__lte=1998, height__gte=160)
    return render_template('search.html', all_services = service)


if __name__ == '__main__':
  app.run(debug=True)
