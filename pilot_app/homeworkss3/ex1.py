from flask import Flask, render_template
from  models.service import Service
import mlab

mlab.connect()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete')
def delete():
    services = Service.objects()
    service_to_delete = Service.objects()
    service_to_delete.delete()
    return "Done"


if __name__ == '__main__':
  app.run(debug=True)
