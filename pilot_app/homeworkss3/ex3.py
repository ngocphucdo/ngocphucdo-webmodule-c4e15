from flask import *
from models.service import Service
import mlab
mlab.connect()
app = Flask(__name__)

@app.route('/show')
def show():
    all_services = Service.objects()
    return render_template('show.html', all_services = all_services)

@app.route('/detail/<abc>')
def detail(abc):
    service_id = Service.objects.get(id = abc)
    return render_template('detail.html', service = service_id)

if __name__ == '__main__':
  app.run(debug=True)
